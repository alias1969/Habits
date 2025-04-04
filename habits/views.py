from rest_framework.generics import (
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
    RetrieveAPIView,
    ListAPIView,
)
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.serializers import ValidationError

from habits.models import Habit
from habits.paginations import HabitPaginator
from habits.permissions import IsOwner
from habits.serializers import HabitSerializer
from habits.services import telegram_message


class HabitCreateAPIView(CreateAPIView):
    """Создание привычки"""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """Отправить сообщение пользователю в Телеграм о создании привычки"""
        habit = serializer.save()
        habit.user = self.request.user
        habit = serializer.save()
        habit.save()
        if habit.user.tg_id:
            telegram_message(habit.user.tg_id, "Создана новая привычка!")


class HabitUpdateAPIView(UpdateAPIView):
    """Изменение привычки"""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_update(self, serializer):
        """Проверка связанной привычки на саму себя"""
        habit = serializer.save()
        if not habit.related_habit and habit.id == habit.related_habit.id:
            raise ValidationError(
                f"Связанная привычка не может быть ссылкой на саму себя!"
            )
        habit.save()


class HabitDeleteAPIView(DestroyAPIView):
    """Удаление привычки"""

    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitRetrieveAPIView(RetrieveAPIView):
    """Просмотр привычки"""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitListAPIView(ListAPIView):
    """Список всех привычек"""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class HabitPublicListAPIView(ListAPIView):
    """Список опубликованных привычек"""

    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(is_public=True)
    permission_classes = [AllowAny]
    pagination_class = HabitPaginator
