from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('services/lawn_care/', views.lawn_care, name='lawn_care'),
    path('services/snow_removal/', views.snow_removal, name='snow_removal'),
    path('services/consultations/', views.consultations, name='consultations'),
]
