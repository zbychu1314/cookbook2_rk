from typing import Any
from django.contrib import admin
from django.http.request import HttpRequest
from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ["author", "title", "content"]
    
    def get_readonly_fields(self, request: HttpRequest, obj: Any | None = ...) -> list[str] | tuple[Any, ...]:
        if request.user.is_superuser:
            return []
        if request.user == obj.author:
            return ["author"]
        
        return self.readonly_fields

    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        if not obj.author:
            obj.author = request.user
        return super().save_model(request, obj, form, change)

admin.site.register(Post, PostAdmin)