#!/usr/bin/env python3
from pathlib import Path


def scan(root: Path) -> list[str]:
    if not root.exists():
        return []
    return [str(p) for p in root.rglob("*") if p.is_file()]


if __name__ == "__main__":
    media_root = Path.home() / "media"
    print(f"Found {len(scan(media_root))} files in {media_root}")
