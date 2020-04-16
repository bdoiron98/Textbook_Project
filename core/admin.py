from django.contrib import admin

from .models import Author, Major, University

admin.site.register(Author)
admin.site.register(Major)
admin.site.register(University)
