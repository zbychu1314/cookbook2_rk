from django.urls import path
from . import views

urlpatterns = [
    
    path("recipes/", views.list, name="list"),
    path("recipes/<int:id>", views.details, name="details")
]