from urllib.parse import parse_qs


def post_start(query_string: str = "") -> dict:
    query = parse_qs(query_string)
    target = query.get("target", ["default"])[0]
    media = query.get("media", [""])[0]
    return {"status": "started", "target": target, "media": media}


def post_stop(query_string: str = "") -> dict:
    query = parse_qs(query_string)
    target = query.get("target", ["default"])[0]
    return {"status": "stopped", "target": target}
