from django.shortcuts import render
from core.services.blogger_service import get_top_bloggers
from core.services.news_service import get_latest_news


def home_view(request):
    context = {
        "top_bloggers": get_top_bloggers(3),
        "latest_news": get_latest_news(5),
    }
    return render(request, "home.html", context)
