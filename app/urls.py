from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("taxi-admin", views.taxi_admin, name="taxi_admin"),
    path("reset",views.reset,name="reset"),
]
