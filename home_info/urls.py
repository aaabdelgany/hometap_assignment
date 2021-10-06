from django.urls import path
from . import views

urlpatterns = [
    path("septic_check",views.septic_check,name="septic_check")
]