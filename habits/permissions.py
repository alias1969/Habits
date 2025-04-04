from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """Проверить является ли пользователь владельцем привычки"""

    message = "Вы не являетесь автором!"

    def has_object_permission(self, request, view, obj):
        if obj.user == request.user:
            return True
        return False
