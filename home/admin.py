from django.contrib import admin
from .models import Articles, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'favicon', 'status')

@admin.register(Articles)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created', 'status')
