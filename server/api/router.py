from handlers.health import get_health
from handlers.launcher import get_now_playing, get_status
from handlers.media import get_browse, get_search
from handlers.playback import post_start, post_stop


def route_get(path: str, query: str) -> tuple[int, dict]:
    if path == "/api/health":
        return 200, get_health()
    if path == "/api/media/browse":
        return 200, get_browse(query)
    if path == "/api/media/search":
        return 200, get_search(query)
    if path == "/api/now-playing":
        return 200, get_now_playing()
    if path == "/api/launcher/status":
        return 200, get_status()
    return 404, {"error": "not found"}


def route_post(path: str) -> tuple[int, dict]:
    if path == "/api/playback/start":
        return 200, post_start()
    if path == "/api/playback/stop":
        return 200, post_stop()
    return 404, {"error": "not found"}
