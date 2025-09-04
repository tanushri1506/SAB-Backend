"""
WSGI config for backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

import django
from django.contrib.auth.models import User

django.setup()

USERNAME = "Tanushri"
EMAIL = "barsainyatanushri555@gmail.com"
PASSWORD = "TypicalGame"

if not User.objects.filter(username=USERNAME).exists():
    User.objects.create_superuser(USERNAME, EMAIL, PASSWORD)
else:
    user = User.objects.get(username=USERNAME)
    user.set_password(PASSWORD)
    user.save()


application = get_wsgi_application()
