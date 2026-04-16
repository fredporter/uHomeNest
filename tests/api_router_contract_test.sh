#!/usr/bin/env bash
set -euo pipefail

python3 - <<'PY'
import sys
from pathlib import Path

sys.path.insert(0, str(Path("server/api").resolve()))
import router

code, payload = router.route_request("GET", "/api/health")
assert code == 200 and payload == {"status": "ok"}

code, payload = router.route_request("GET", "/api/media/browse", "path=%2Fmovies")
assert code == 200 and payload["path"] == "/movies" and "items" in payload

code, payload = router.route_request("GET", "/api/media/search", "q=matrix")
assert code == 200 and payload["query"] == "matrix" and "results" in payload

code, payload = router.route_request("POST", "/api/playback/start")
assert code == 200 and payload["status"] == "started"

code, payload = router.route_request("POST", "/api/playback/stop")
assert code == 200 and payload["status"] == "stopped"

code, payload = router.route_request("GET", "/api/unknown")
assert code == 404 and payload["error"] == "not found"

code, payload = router.route_request("PUT", "/api/health")
assert code == 405 and payload["error"] == "method not allowed"

print("api router contract test passed")
PY
