from django.urls import path
from .views import my_info

urlpatterns = [
    path('my-info/', my_info),
]
