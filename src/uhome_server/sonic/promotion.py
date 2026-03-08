"""Promote executed uHOME install assets onto a host-style filesystem layout."""

from __future__ import annotations

import json
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from uhome_server.config import utc_now_iso_z


def _write_json(path: Path, payload: dict[str, Any]) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return path


def _copy_tree(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists():
        shutil.rmtree(destination)
    shutil.copytree(source, destination, symlinks=True)


@dataclass(frozen=True)
class PromotionResult:
    target_root: Path
    host_root: Path
    snapshot_root: Path
    promoted_paths: list[str]
    receipt_path: Path
    state_path: Path

    def to_dict(self) -> dict[str, Any]:
        return {
            "target_root": str(self.target_root),
            "host_root": str(self.host_root),
            "snapshot_root": str(self.snapshot_root),
            "promoted_paths": self.promoted_paths,
            "receipt_path": str(self.receipt_path),
            "state_path": str(self.state_path),
        }


@dataclass(frozen=True)
class RollbackResult:
    host_root: Path
    snapshot_root: Path
    restored_paths: list[str]
    state_path: Path

    def to_dict(self) -> dict[str, Any]:
        return {
            "host_root": str(self.host_root),
            "snapshot_root": str(self.snapshot_root),
            "restored_paths": self.restored_paths,
            "state_path": str(self.state_path),
        }


_PROMOTION_MAPPINGS: tuple[tuple[str, str], ...] = (
    ("install-root", "opt/uhome"),
    ("config", "opt/uhome/config"),
    ("etc/uhome", "etc/uhome"),
    ("systemd/system", "etc/systemd/system"),
    ("systemd/multi-user.target.wants", "etc/systemd/system/multi-user.target.wants"),
    ("systemd/graphical.target.wants", "etc/systemd/system/graphical.target.wants"),
    ("bin", "opt/uhome/bin"),
    ("receipts", "var/lib/uhome/receipts"),
    ("state", "var/lib/uhome/state"),
    ("rollback", "var/lib/uhome/rollback"),
)


def promote_target_root(target_root: Path, host_root: Path) -> PromotionResult:
    if not target_root.exists():
        raise ValueError(f"Target root does not exist: {target_root}")
    snapshot_root = host_root / "var" / "lib" / "uhome" / "snapshots" / "latest"
    snapshot_root.mkdir(parents=True, exist_ok=True)

    promoted_paths: list[str] = []
    for source_rel, dest_rel in _PROMOTION_MAPPINGS:
        source = target_root / source_rel
        if not source.exists():
            continue
        destination = host_root / dest_rel
        snapshot = snapshot_root / dest_rel
        if destination.exists():
            if snapshot.exists():
                shutil.rmtree(snapshot)
            snapshot.parent.mkdir(parents=True, exist_ok=True)
            if destination.is_dir():
                shutil.copytree(destination, snapshot, symlinks=True)
            else:
                shutil.copy2(destination, snapshot)
        if source.is_dir():
            _copy_tree(source, destination)
        else:
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)
        promoted_paths.append(str(destination))

    receipt_path = _write_json(
        host_root / "var" / "lib" / "uhome" / "promotion-receipt.json",
        {
            "promoted_at": utc_now_iso_z(),
            "target_root": str(target_root),
            "host_root": str(host_root),
            "snapshot_root": str(snapshot_root),
            "promoted_paths": promoted_paths,
        },
    )
    state_path = _write_json(
        host_root / "var" / "lib" / "uhome" / "promotion-state.json",
        {
            "status": "applied",
            "applied_at": utc_now_iso_z(),
            "target_root": str(target_root),
            "snapshot_root": str(snapshot_root),
            "promoted_paths": promoted_paths,
        },
    )
    return PromotionResult(
        target_root=target_root,
        host_root=host_root,
        snapshot_root=snapshot_root,
        promoted_paths=promoted_paths,
        receipt_path=receipt_path,
        state_path=state_path,
    )


def rollback_promoted_target(host_root: Path) -> RollbackResult:
    snapshot_root = host_root / "var" / "lib" / "uhome" / "snapshots" / "latest"
    if not snapshot_root.exists():
        raise ValueError(f"Snapshot root does not exist: {snapshot_root}")

    restored_paths: list[str] = []
    for _, dest_rel in _PROMOTION_MAPPINGS:
        snapshot = snapshot_root / dest_rel
        destination = host_root / dest_rel
        if not snapshot.exists():
            continue
        if destination.exists():
            if destination.is_dir():
                shutil.rmtree(destination)
            else:
                destination.unlink()
        if snapshot.is_dir():
            _copy_tree(snapshot, destination)
        else:
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(snapshot, destination)
        restored_paths.append(str(destination))

    state_path = _write_json(
        host_root / "var" / "lib" / "uhome" / "promotion-state.json",
        {
            "status": "rolled_back",
            "rolled_back_at": utc_now_iso_z(),
            "snapshot_root": str(snapshot_root),
            "restored_paths": restored_paths,
        },
    )
    return RollbackResult(
        host_root=host_root,
        snapshot_root=snapshot_root,
        restored_paths=restored_paths,
        state_path=state_path,
    )
