#!/usr/bin/env bash
set -euo pipefail

python3 ./server/media/scanner.py >/dev/null
echo "media scan test passed"
