from django.contrib import admin
from .models import Hint, UserQuastion, Articles


@admin.register(UserQuastion)
class UserQuastionAdmin(admin.ModelAdmin):
    list_display = ('issue', 'child_name', 'description', 'email', 'phone')


@admin.register(Hint)
class HintAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created', 'status', 'is_delete')


@admin.register(Articles)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created', 'status')