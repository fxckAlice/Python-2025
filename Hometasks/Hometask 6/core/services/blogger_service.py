from core.repository.blogger_repository import (
    fetch_all_bloggers,
    fetch_blogger_by_id as repo_get_by_id,
    fetch_blogger_by_slug as repo_get_by_slug
)


def get_all_bloggers(category=None, limit=None):
    bloggers = fetch_all_bloggers()
    if category:
        bloggers = [b for b in bloggers if b["category"] == category]
    if limit:
        bloggers = bloggers[:limit]
    return bloggers


def get_blogger_by_id(blogger_id):
    return repo_get_by_id(blogger_id)


def get_blogger_by_slug(slug):
    return repo_get_by_slug(slug)


def get_top_bloggers(n):
    bloggers = fetch_all_bloggers()
    bloggers = sorted(bloggers, key=lambda b: b["followers_count"], reverse=True)
    return bloggers[:n]
