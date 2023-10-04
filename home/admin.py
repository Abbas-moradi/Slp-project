from django.contrib import admin
from .models import ImageGallery, NewsUserEmail


@admin.register(ImageGallery)
class ImageGalleryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'status')


@admin.register(NewsUserEmail)
class UserNewsEmailAdmin(admin.ModelAdmin):
    list_display = ('email', 'created', 'status')