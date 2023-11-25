from django.urls import path
from . import views

app_name = "posts" 
urlpatterns = [
    path("posts/", views.list, name="list"),
    path("posts/<int:id>/", views.details, name="details"),
    path("posts/add/", views.add, name="add"),
  
]
