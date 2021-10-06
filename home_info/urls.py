from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("septic_check",views.septic_check,name="septic_check")
]