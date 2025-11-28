from django.shortcuts import render
from core.services.blogger_service import (
    get_all_bloggers,
    get_blogger_by_id,
    get_blogger_by_slug
)
from core.services.publication_service import get_publications_for_blogger
from core.controllers.error_controller import error_404_view


def blogger_list_view(request):
    category = request.GET.get("category")
    limit = request.GET.get("limit")
    limit = int(limit) if limit else None

    bloggers = get_all_bloggers(category, limit)

    context = {
        "bloggers": bloggers,
        "request": request
    }

    return render(request, "bloggers.html", context)


def blogger_detail_view(request, id):
    blogger = get_blogger_by_id(id)
    if not blogger:
        return error_404_view(request)

    publications = get_publications_for_blogger(id)

    context = {
        "blogger": blogger,
        "publications": publications
    }

    return render(request, "blogger_detail.html", context)



def blogger_detail_by_slug_view(request, slug):
    blogger = get_blogger_by_slug(slug)
    if not blogger:
        return error_404_view(request)
    return blogger_detail_view(request, blogger["id"])

