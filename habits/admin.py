from django.contrib import admin

from habits.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    """Панель привычки в админке"""

    list_display = (
        "user",
        "action",
    )
