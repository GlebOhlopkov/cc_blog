from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            username='admin',
            birthday='1980-01-01',
            is_superuser=True,
            is_staff=True,
            is_active=True,
        )

        user.set_password('admin')
        user.save()