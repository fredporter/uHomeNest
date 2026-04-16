#!/usr/bin/env python3
import time
from pathlib import Path


def watch(root: Path, interval: int = 5) -> None:
    print(f"Watching {root} every {interval}s (placeholder)")
    while True:
        time.sleep(interval)


if __name__ == "__main__":
    watch(Path.home() / "media")
