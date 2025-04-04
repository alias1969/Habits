from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from user.models import User


class HabitTestCase(APITestCase):
    """Тестирование CRUD привычек."""

    def setUp(self):
        self.user = User.objects.create(email="test@mail.ru")
        self.habit = Habit.objects.create(
            user=self.user,
            location="дома",
            time="2025-03-31T18:31:00+03:00",
            action="сделать отжимание 25 раз",
            is_useful_habit="True",
            periodicity=1,
            reward="Null",
            time_to_complete="00:02:00",
        )
        self.client.force_authenticate(user=self.user)

    def test_habit_list(self):
        url = reverse("habits:habit_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_habit_create(self):
        url = reverse("habits:habit_create")
        data = {
            #"user": self.user.pk,
            "location": "дома",
            "time": "2025-03-31T18:32:00+03:00",
            "action": "выпить кофе",
            "is_useful_habit": "False",
            "periodicity": 1,
            "time_to_complete": "00:02:00",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 2)

    def test_habit_retrieve(self):
        url = reverse("habits:habit_retrieve", args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("periodicity"), self.habit.periodicity)

    def test_habit_update(self):
        url = reverse("habits:habit_update", args=(self.habit.pk,))
        data = {
            "location": "на улице",
            "time": "2025-03-31T18:32:00+03:00",
            "action": "прогуляться",
            "is_useful_habit": False,
            "periodicity": 1,
            "time_to_complete": "00:02:00",
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("location"), "на улице")

    def test_habit_delete(self):
        url = reverse("habits:habit_delete", args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 0)

    def test_habit_public_list(self):
        url = reverse("habits:habit_public")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
