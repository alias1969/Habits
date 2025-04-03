from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenRefreshView

from user.apps import UserConfig
from user.views import UserCreateAPIView, UserUpdateAPIView, UserDeleteAPIView, UserListAPIView, UserRetrieveAPIView, \
    UserTokenObtainPairView

app_name = UserConfig.name

urlpatterns = [
    path('', UserListAPIView.as_view(), name='user_list'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='user_update'),
    path('delete/<int:pk>/', UserDeleteAPIView.as_view(), name='user_delete'),
    path('viewing/<int:pk>/', UserRetrieveAPIView.as_view(), name='user_viewing'),
    path('login/', UserTokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes=(AllowAny,)), name='token_refresh'),
]