from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('newLand/', views.land_new, name="land_new"),   
]
