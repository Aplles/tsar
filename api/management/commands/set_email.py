import uuid

from django.core.management.base import BaseCommand, CommandError

from api.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        for user in User.objects.all():
            if not user.email:
                user.email = f"{uuid.uuid4()}@mail.ru"
                user.save()
