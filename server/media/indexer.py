#!/usr/bin/env python3
import json
from pathlib import Path


def build_index(media_root: Path) -> dict:
    files = [str(p) for p in media_root.rglob("*") if p.is_file()] if media_root.exists() else []
    return {"root": str(media_root), "count": len(files), "files": files}


if __name__ == "__main__":
    root = Path.home() / "media"
    output = root / ".media-index.json"
    output.write_text(json.dumps(build_index(root), indent=2), encoding="utf-8")
    print(f"Wrote {output}")
