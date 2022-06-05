from django.contrib import admin
from .models import Follow, Post,Profile, Comment

# Register your models here.
admin.site.register(Follow)
admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Comment)