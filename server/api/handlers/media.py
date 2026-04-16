from urllib.parse import parse_qs


def get_browse(query_string: str) -> dict:
    query = parse_qs(query_string)
    return {"path": query.get("path", ["~"])[0], "items": []}


def get_search(query_string: str) -> dict:
    query = parse_qs(query_string)
    return {"query": query.get("q", [""])[0], "results": []}
