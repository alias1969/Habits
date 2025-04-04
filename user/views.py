from rest_framework.generics import (
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
)

from user.models import User
from user.serializer import UserSerializer, UserTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny, IsAuthenticated


class UserCreateAPIView(CreateAPIView):
    """Регистрация нового пользователя"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        """Активация учетной записи пользователя"""
        user = serializer.save(is_active=True)
        user.set_password(self.request.data.get("password"))
        user.save()


class UserUpdateAPIView(UpdateAPIView):
    """Изменение профиля пользователя"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def password_update(self, serializer):
        """Обновление и сохранение пароля при изменении"""
        user = serializer.save()
        user.set_password(self.request.data.get("password"))
        user.save()


class UserDeleteAPIView(DestroyAPIView):
    """Удаление пользователя"""

    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class UserListAPIView(ListAPIView):
    """Список профилей"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class UserRetrieveAPIView(RetrieveAPIView):
    """Карточка пользователя"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class UserTokenObtainPairView(TokenObtainPairView):
    """Получение токена"""

    serializer_class = UserTokenObtainPairSerializer
