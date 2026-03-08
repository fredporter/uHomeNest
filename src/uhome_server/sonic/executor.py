"""Execute staged uHOME installer artifacts into a target root."""

from __future__ import annotations

import json
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from uhome_server.config import utc_now_iso_z


def _read_json(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"Expected JSON object in {path}")
    return payload


def _write_json(path: Path, payload: dict[str, Any]) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return path


def _sanitize_unit_name(name: str) -> str:
    return name.strip().replace("/", "-")


def _service_unit(service_name: str, install_root: str) -> str:
    unit_name = _sanitize_unit_name(service_name)
    return "\n".join(
        [
            "[Unit]",
            f"Description={unit_name} for uHOME",
            "After=network-online.target",
            "",
            "[Service]",
            "Type=simple",
            f"WorkingDirectory={install_root}",
            f"ExecStart=/usr/bin/env sh -lc 'echo Starting {unit_name} from {install_root}; sleep infinity'",
            "Restart=on-failure",
            "",
            "[Install]",
            "WantedBy=multi-user.target",
            "",
        ]
    )


@dataclass(frozen=True)
class ExecutionResult:
    stage_dir: Path
    target_root: Path
    installed_components: list[str]
    config_paths: list[str]
    service_unit_paths: list[str]
    receipt_path: Path
    state_path: Path
    rollback_path: Path | None

    def to_dict(self) -> dict[str, Any]:
        return {
            "stage_dir": str(self.stage_dir),
            "target_root": str(self.target_root),
            "installed_components": self.installed_components,
            "config_paths": self.config_paths,
            "service_unit_paths": self.service_unit_paths,
            "receipt_path": str(self.receipt_path),
            "state_path": str(self.state_path),
            "rollback_path": None if self.rollback_path is None else str(self.rollback_path),
        }


def execute_staged_install(stage_dir: Path, target_root: Path) -> ExecutionResult:
    plan = _read_json(stage_dir / "install-plan.json")
    if not plan.get("ready", False):
        raise ValueError("Staged install plan is not ready.")

    receipt = _read_json(stage_dir / "install-receipt.json")
    config_dir = stage_dir / "config"
    components_dir = stage_dir / "components"
    rollback_source = stage_dir / "rollback" / "rollback.json"

    install_root = target_root / "install-root"
    state_root = target_root / "state"
    config_root = target_root / "config"
    services_root = target_root / "systemd"
    receipts_root = target_root / "receipts"
    rollback_root = target_root / "rollback"
    for path in (install_root, state_root, config_root, services_root, receipts_root):
        path.mkdir(parents=True, exist_ok=True)

    installed_components: list[str] = []
    if components_dir.exists():
        for component_dir in sorted(components_dir.iterdir(), key=lambda item: item.name):
            if not component_dir.is_dir():
                continue
            target_component_dir = install_root / component_dir.name
            target_component_dir.mkdir(parents=True, exist_ok=True)
            for artifact in sorted(component_dir.iterdir(), key=lambda item: item.name):
                shutil.copy2(artifact, target_component_dir / artifact.name)
            installed_components.append(component_dir.name)

    config_paths: list[str] = []
    service_unit_paths: list[str] = []
    service_names: list[str] = []
    if config_dir.exists():
        for config_path in sorted(config_dir.glob("*.json")):
            payload = _read_json(config_path)
            target_config = config_root / config_path.name
            _write_json(target_config, payload)
            config_paths.append(str(target_config))
            service_name = payload.get("service_name")
            if isinstance(service_name, str) and service_name.strip():
                service_names.append(service_name.strip())

    for service_name in sorted(set(service_names)):
        unit_path = services_root / f"{_sanitize_unit_name(service_name)}.service"
        unit_path.write_text(_service_unit(service_name, receipt.get("install_root", "/opt/uhome")), encoding="utf-8")
        service_unit_paths.append(str(unit_path))

    receipt_payload = {
        **receipt,
        "executed_at": utc_now_iso_z(),
        "target_root": str(target_root),
        "installed_components": installed_components,
        "service_unit_paths": service_unit_paths,
    }
    receipt_path = _write_json(receipts_root / "install-receipt.json", receipt_payload)

    state_path = _write_json(
        state_root / "install-state.json",
        {
            "executed_at": utc_now_iso_z(),
            "stage_dir": str(stage_dir),
            "target_root": str(target_root),
            "status": "installed",
            "installed_components": installed_components,
            "service_unit_paths": service_unit_paths,
            "plan_steps": plan.get("steps", []),
        },
    )

    rollback_path = None
    if rollback_source.exists():
        rollback_root.mkdir(parents=True, exist_ok=True)
        rollback_path = rollback_root / "rollback.json"
        shutil.copy2(rollback_source, rollback_path)

    return ExecutionResult(
        stage_dir=stage_dir,
        target_root=target_root,
        installed_components=installed_components,
        config_paths=config_paths,
        service_unit_paths=service_unit_paths,
        receipt_path=receipt_path,
        state_path=state_path,
        rollback_path=rollback_path,
    )
