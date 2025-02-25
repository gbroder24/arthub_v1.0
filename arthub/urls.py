"""arthub URL Configuration

The `urlpatterns` list routes URLs to views.
For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function:
    from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    page_not_found,
    server_error,
    bad_request,
    permission_denied
)

handler404 = 'config.views.page_not_found'
handler403 = 'config.views.permission_denied'
handler400 = 'config.views.bad_request'
handler500 = 'config.views.server_error'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('products/', include('products.urls')),
    path('bag/', include('bag.urls')),
    path('checkout/', include('checkout.urls')),
    path('profile/', include('profiles.urls')),
    path('faq/', include('faq.urls')),
    path('contact/', include('contact.urls')),
    path('newsletter/', include('newsletter.urls')),
    # Simulate 404 error (Page Not Found)
    path('trigger-404/', page_not_found, name='trigger-404'),

    # Simulate 500 error (Server Error)
    path('trigger-500/', server_error, name='trigger-500'),

    # Simulate 400 error (Bad Request)
    path('trigger-400/', bad_request, name='trigger-400'),

    # Simulate 403 error (Forbidden)
    path('trigger-403/', permission_denied, name='trigger-403'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
