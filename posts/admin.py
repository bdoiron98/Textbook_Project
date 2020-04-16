from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Post
from core.models import Textbook

# admin.site.register(Author)
# admin.site.register(Major)
# admin.site.register(University)
# admin.site.register(Textbook)

admin.site.register(Post)
admin.site.register(Textbook)
