from django.contrib import admin
from .models import Recipe

# @admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "short_descriptiopn"]
    
    
    def short_descriptiopn(self, obj):
        return obj.description[:20] + "..."
    

    def get_list_display(self, request):
        """
        Return a sequence containing the fields to be displayed on the
        changelist.
        """
        if request.user.is_superuser is False:
            return ["title"]
        return self.list_display

admin.site.register(Recipe, RecipeAdmin)