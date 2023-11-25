from django.shortcuts import render

from .models import Recipe

# Create your views here.

def list(request):
    return render(
        request, 
        "recipes/list.html",
        {"recipes": Recipe.objects.all()}
    )