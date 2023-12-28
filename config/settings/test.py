from .base import *  # noqa

DJANGO_SETTINGS_MODULE = "config.settings.test"

DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}
