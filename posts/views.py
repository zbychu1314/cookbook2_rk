from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post


# adres -> funkcja -> szablon
# posts -> list -> posts/list.html

def list(request):
    return render(
        request,
        "posts/list.html",
        {"posts": Post.objects.filter(published=True)}
    )

# posts/<int:id> -> details -> posts/details.html
def details(request, id):
    
    return render(
        request,
        "posts/details.html",
        {"post": Post.objects.get(id=id)}
    )

# GET posts/add -> create -> posts/add.html tu trzeba utworzyc formularz <form method="POST">
# POST posts/add -> create -> operacj dodania a nastepnie redirect

@login_required
def add(request):
    # if not request.user.is_authenticated:
    #     return HttpResponse("Zaloguj sie by dodac post")
    
    
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        author = request.user
        
        Post.objects.create(title=title, content=content, author=author, published=True)
        
        return redirect("posts:list")
    
    return render(
        request, 
        "posts/add.html"
    )
    
    