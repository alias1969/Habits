from django.contrib import admin

from user.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Пользователи в админке"""
    list_display = ('email', 'id', 'phone', 'tg_id')
