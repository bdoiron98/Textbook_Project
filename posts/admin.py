from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Post, Textbook



@admin.register(Textbook)
class TextbookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    ordering = ('title',)


admin.site.register(Post)
# admin.site.register(Textbook)
