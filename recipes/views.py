from django.shortcuts import render, redirect

from .models import Recipe

# Create your views here.

def list(request):
    return render(
        request, 
        "recipes/list.html",
        {"recipes": Recipe.objects.all()}
    )
    
    
def details(request, id):
    """
    /recipes/1 -> /recipes
    """
    return redirect("/recipes/")