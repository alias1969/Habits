from django.urls import path

from habits.apps import HabitsConfig
from habits.views import (
    HabitListAPIView,
    HabitCreateAPIView,
    HabitUpdateAPIView,
    HabitDeleteAPIView,
    HabitRetrieveAPIView,
    HabitPublicListAPIView,
)

app_name = HabitsConfig.name

urlpatterns = [
    path("", HabitListAPIView.as_view(), name="habit_list"),
    path("create/", HabitCreateAPIView.as_view(), name="habit_create"),
    path("update/<int:pk>/", HabitUpdateAPIView.as_view(), name="habit_update"),
    path("delete/<int:pk>/", HabitDeleteAPIView.as_view(), name="habit_delete"),
    path("retrieve/<int:pk>/", HabitRetrieveAPIView.as_view(), name="habit_retrieve"),
    path("public/", HabitPublicListAPIView.as_view(), name="habit_public"),
]
