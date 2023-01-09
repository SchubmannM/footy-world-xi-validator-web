"""
ASGI config for core_service project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")
os.environ.setdefault("DJANGO_CONFIGURATION", "Dev")

from configurations.asgi import get_asgi_application

application = get_asgi_application()
