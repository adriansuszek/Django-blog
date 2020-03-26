from django.contrib import admin

# Register your models here.
from .models import Author, Category, Post

admin.site.register(Author)
admin.site.register(Category)
# admin.site.register(Post)

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, PostAdmin)
