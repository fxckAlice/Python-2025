"""
URL configuration for bloggers_platform project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path

from core.controllers.home_controller import home_view
from core.controllers.blogger_controller import (
    blogger_list_view,
    blogger_detail_view,
    blogger_detail_by_slug_view
)
from core.controllers.news_controller import (
    news_redirect_view,
    news_old_redirect_view
)
from core.controllers.publication_controller import (
    publications_list_view,
    publication_detail_view,
    blogger_publications_view
)

from core.controllers.error_controller import error_404_view


urlpatterns = [
    path('', home_view),

    path('bloggers/', blogger_list_view),
    path('bloggers/<int:id>/', blogger_detail_view),

    re_path(r'^blogger/(?P<slug>[a-z0-9-_]+)/$', blogger_detail_by_slug_view),

    path('news/', news_redirect_view),
    re_path(r'^old-news/.*$', news_old_redirect_view),

    path("publications/", publications_list_view, name="publications_list"),
    path("publications/<int:id>/", publication_detail_view, name="publication_detail"),
    path("bloggers/<int:blogger_id>/publications/", blogger_publications_view, name="blogger_publications"),

]

handler404 = error_404_view

