"""Registering Model Here"""
from django.contrib import admin
from .models import Post

# Register your models here.
# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post Model Registered here for Admin Panel"""
    list_display = [ 'title', 'author', 'id',]
