from django.db import models
from django.contrib.auth.models import AbstractUser

NULLABLE = {"null": True, "blank": True}


class User(AbstractUser):
    username = None

    email = models.EmailField(
        unique=True, verbose_name="Почта", help_text="Уакжите e-mail"
    )
    phone = models.CharField(
        max_length=35,
        verbose_name="Номер телефона",
        help_text="Укажите номер телефона",
        **NULLABLE,
    )
    city = models.CharField(
        max_length=50, verbose_name="Город", help_text="Укажите город"
    )
    avatar = models.ImageField(
        upload_to="users/avatars",
        verbose_name="Аватар",
        help_text="Загружите фото",
        **NULLABLE,
    )
    tg_id = models.CharField(
        max_length=50, verbose_name="Telergram chat_id", **NULLABLE
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"{self.email}"
