from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContactFormCreateView.as_view(), name='contact-form'),
    path('success/', views.ContactSuccess, name='contact-success'),

]
