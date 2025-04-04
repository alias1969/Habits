from django.conf import settings
from django.db import models

NULLABLE = {"blank": True, "null": True}


class Habit(models.Model):
    """Модель привычки"""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        help_text="Создатель привычки",
        **NULLABLE,
    )
    location = models.CharField(
        max_length=250,
        default="Дома",
        verbose_name="Место",
        help_text="Место, в котором необходимо выполнять привычку",
    )
    time = models.DateTimeField(
        verbose_name="Время",
        help_text="Время, когда необходимо выполнять привычку",
    )
    action = models.CharField(
        max_length=250,
        verbose_name="Действие",
        help_text="Действие, которое представляет собой привычка",
    )
    is_useful_habit = models.BooleanField(
        default=False,
        verbose_name="Признак приятной привычки",
        help_text="Привычка, которую можно привязать к выполнению полезной привычки",
    )
    related_habit = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        verbose_name="Связанная привычка",
        help_text="Привычка, которая связана с другой привычкой, "
        "важно указывать для полезных привычек, но не для приятных",
        **NULLABLE,
    )
    periodicity = models.PositiveIntegerField(
        verbose_name="Периодичность",
        help_text="Периодичность выполнения привычки для напоминания в днях",
    )
    reward = models.CharField(
        max_length=200,
        verbose_name="Вознаграждение",
        help_text="Чем пользователь должен себя вознаградить после выполнения",
        **NULLABLE,
    )
    time_to_complete = models.DurationField(
        verbose_name="Время на выполнение",
        help_text="Время, которое предположительно потратит пользователь на выполнение привычки",
    )
    is_public = models.BooleanField(
        default=True,
        verbose_name="Признак публичности",
        help_text="Привычки можно публиковать в общий доступ, "
        "чтобы другие пользователи могли брать в пример чужие привычк",
    )

    def __str__(self):
        return f"{self.user} - {self.action}"

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
