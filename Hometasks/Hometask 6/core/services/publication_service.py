from core.repository.publication_repository import (
    fetch_all_publications,
    fetch_publication_by_id,
    fetch_publications_by_blogger_id,
)


def get_all_publications(limit=None):
    result = fetch_all_publications()
    if limit:
        result = result[:limit]
    return result


def get_publication_by_id(publication_id):
    return fetch_publication_by_id(publication_id)




def get_publications_for_blogger(blogger_id, limit=None):
    result = fetch_publications_by_blogger_id(blogger_id)
    if limit:
        result = result[:limit]
    return result


def get_latest_publications(limit=None):
    result = sorted(fetch_all_publications(), key=lambda p: p["published_at"], reverse=True)
    if limit:
        result = result[:limit]
    return result


def get_latest_publications_by_blogger_id(blogger_id, limit=None):
    result = fetch_publications_by_blogger_id(blogger_id)
    result = sorted(result, key=lambda p: p["published_at"], reverse=True)
    if limit:
        result = result[:limit]
    return result
