from django.core.management import BaseCommand

from user.models import User


class Command(BaseCommand):
    """ Команда для создания суперпользователя """
    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@sky.pro',
            first_name='Admin',
            is_superuser=True,
            is_active=True,
            is_staff=True,
        )

        user.set_password('123')
        user.save()