from django.shortcuts import render
from django.http import HttpResponseServerError


def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, "errors/404.html", status=404)


def handler500(request):
    """ Error Handler 500 - Server Error """
    return render(request, "errors/500.html", status=500)


def trigger_500(request):
    # This will intentionally raise an exception and trigger the 500 error handler
    raise Exception("Intentional 500 error for testing purposes.")
