from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import parse_qs, urlparse


class Handler(BaseHTTPRequestHandler):
    def _json(self, payload: dict, code: int = 200) -> None:
        body = json.dumps(payload).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:  # noqa: N802
        parsed = urlparse(self.path)
        if parsed.path == "/api/health":
            self._json({"status": "ok"})
            return
        if parsed.path == "/api/media/browse":
            query = parse_qs(parsed.query)
            self._json({"path": query.get("path", ["~"])[0], "items": []})
            return
        if parsed.path == "/api/media/search":
            query = parse_qs(parsed.query)
            self._json({"query": query.get("q", [""])[0], "results": []})
            return
        if parsed.path == "/api/now-playing":
            self._json({"state": "idle"})
            return
        if parsed.path == "/api/launcher/status":
            self._json({"surface": "uhome-launcher", "status": "ready"})
            return
        self._json({"error": "not found"}, 404)

    def do_POST(self) -> None:  # noqa: N802
        if self.path == "/api/playback/start":
            self._json({"status": "started"})
            return
        if self.path == "/api/playback/stop":
            self._json({"status": "stopped"})
            return
        self._json({"error": "not found"}, 404)


def run() -> None:
    server = HTTPServer(("127.0.0.1", 7890), Handler)
    print("uHomeNest API listening on http://127.0.0.1:7890")
    server.serve_forever()


if __name__ == "__main__":
    run()
