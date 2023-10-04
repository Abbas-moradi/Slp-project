from django.contrib import admin
from .models import Hint, UserQuastion, Articles, Category, SmallDescription


@admin.register(UserQuastion)
class UserQuastionAdmin(admin.ModelAdmin):
    list_display = ('issue', 'child_name', 'description', 'email', 'phone')


@admin.register(Hint)
class HintAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created', 'status', 'is_delete')


@admin.register(Articles)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created', 'status')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'favicon', 'color_status', 'status')


@admin.register(SmallDescription)
class SmallDescriptionAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'status')