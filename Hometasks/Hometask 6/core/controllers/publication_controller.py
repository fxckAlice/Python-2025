from django.shortcuts import render
from core.services.publication_service import get_all_publications
from core.services.publication_service import get_publication_by_id
from core.services.publication_service import get_publications_for_blogger
from core.services.blogger_service import get_all_bloggers
from core.services.blogger_service import get_blogger_by_id
from core.controllers.error_controller import error_404_view

def blogger_publications_view(request, blogger_id):
    blogger = get_blogger_by_id(blogger_id)
    if not blogger:
        return error_404_view(request)

    publications = get_publications_for_blogger(blogger_id)

    context = {
        "blogger": blogger,
        "publications": publications
    }

    return render(request, "blogger_publications.html", context)

def publication_detail_view(request, id):
    publication = get_publication_by_id(id)

    if not publication:
        return error_404_view(request)

    context = {
        "publication": publication
    }

    return render(request, "publication_detail.html", context)


def publications_list_view(request):
    publications = get_all_publications()
    bloggers = get_all_bloggers()

    for p in publications:
        p["blogger"] = next((b for b in bloggers if b["id"] == p["blogger_id"]), None)

    return render(request, "publications.html", {
        "publications": publications,
    })

