from django.contrib import admin
from .models import Category, ImageGallery, NewsUserEmail


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'favicon', 'color_status', 'status')


@admin.register(ImageGallery)
class ImageGalleryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'status')


@admin.register(NewsUserEmail)
class UserNewsEmailAdmin(admin.ModelAdmin):
    list_display = ('email', 'created', 'status')