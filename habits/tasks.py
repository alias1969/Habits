from datetime import datetime, timedelta

import pytz
from celery import shared_task
from django.conf import settings
from django.utils import timezone

from habits.models import Habit
from habits.services import telegram_message


@shared_task()
def telegram_message_list():
    """Предупреждение о выполнении привычки"""
    timezone.activate(pytz.timezone(settings.CELERY_TIMEZONE))
    zone = pytz.timezone(settings.CELERY_TIMEZONE)
    # текущее дата и время
    now = datetime.now(zone)
    habits = Habit.objects.all()

    for habit in habits:
        user_tg = habit.user.tg_id  # telegram chat bott id
        if (
                user_tg
                and now >= habit.habit_time - timedelta(minutes=10)
                and now.date() == habit.habit_time.date()
        ):
            if habit.is_nice:
                message = (f"Молодец - ты заслужил {habit.action} в {habit.habit_time + timedelta(hours=3)} "
                           f"{habit.location}")
            else:
                message = (
                    f"Не забудь {habit.action} в {habit.habit_time + timedelta(hours=3)} {habit.location}"
                )

            telegram_message(user_tg, message)

            if habit.present:
                telegram_message(
                    user_tg, f"Молодец! Ты заслужил награду: {habit.present}"
                )

            habit.habit_time += timedelta(days=habit.period)
            habit.save()

