from django.contrib import admin
from .models import Post

# Use syntax below to register your models on the admin page
admin.site.register(Post)