import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

from django.contrib.auth.models import User

# Replace these with your desired credentials
USERNAME = "Tanushri"
EMAIL = "barsainyatanushri555@gmail.com"
PASSWORD = "TypicalGame"

if not User.objects.filter(username=USERNAME).exists():
    User.objects.create_superuser(USERNAME, EMAIL, PASSWORD)
    print("Superuser created successfully!")
else:
    user = User.objects.get(username=USERNAME)
    user.set_password(PASSWORD)
    user.save()
    print("Password updated successfully!")
