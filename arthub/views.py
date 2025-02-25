from django.shortcuts import render
from django.http import HttpResponseBadRequest


def handler400(request):
    """ Error Handler 400 - Bad Request """
    return render(request, "errors/400.html", status=400)


def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, "errors/404.html", status=404)


def handler500(request):
    """ Error Handler 500 - Server Error """
    return render(request, "errors/500.html", status=500)


def trigger_400(request):
    # This will intentionally raise an exception and trigger the 400 error handler
    raise HttpResponseBadRequest("Intentional 400 error for testing purposes.")
