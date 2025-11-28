from django.shortcuts import render


def error_404_view(request, exception=None):
    context = {
        "message": "Blogger not found" if "blogger" in (request.path or "") else "Page not found"
    }
    return render(request, "error_404.html", context, status=404)


def error_500_view(request):
    return render(request, "error_404.html", {"message": "Server error"}, status=500)
