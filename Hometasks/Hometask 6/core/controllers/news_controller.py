from django.http import JsonResponse, HttpResponseRedirect


def news_redirect_view(request):
    return HttpResponseRedirect("/")


def news_old_redirect_view(request, path=None):
    return HttpResponseRedirect("/")
