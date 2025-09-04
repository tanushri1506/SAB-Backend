from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Creates or resets the admin user'

    def handle(self, *args, **options):
        USERNAME = "Tanushri"
        EMAIL = "barsainyatanushri555@gmail.com"
        PASSWORD = "TypicalGame"

        if not User.objects.filter(username=USERNAME).exists():
            User.objects.create_superuser(USERNAME, EMAIL, PASSWORD)
            self.stdout.write(self.style.SUCCESS('Admin user created'))
        else:
            user = User.objects.get(username=USERNAME)
            user.set_password(PASSWORD)
            user.save()
            self.stdout.write(self.style.SUCCESS('Admin password updated'))
