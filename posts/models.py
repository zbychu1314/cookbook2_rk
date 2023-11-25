from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(
        verbose_name="tytuł",
        max_length=255)
    content = models.TextField()
    published = models.BooleanField()
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    
    