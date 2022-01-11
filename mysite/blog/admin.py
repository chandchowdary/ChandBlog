from django.contrib import admin
from blog.models import Post, Comment

#commnet
admin.site.register(Post)
admin.site.register(Comment)
