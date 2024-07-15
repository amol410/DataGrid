"""Creating models here so they can interact with databases and views"""
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    """We have Model here to create Post for Database Creation"""
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)

    # def __str__(self):
    #     """Displaying information on Admin"""
    #     return self.title