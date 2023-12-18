from django.contrib import admin
from django.urls import path
from birthday import views

urlpatterns = [
    path('', views.home),
    path('wish/', views.wish, name='wish'),
    path('thankyou/', views.thankyou, name='thankyou')
]