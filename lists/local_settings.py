import os

DEBUG = True
TEMPLATE_DEBUG = True

## development
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "movies_db",
        "USER": "admin",
        "PASSWORD": "$h@wshank!",
        "HOST": "",
        "PORT": "",
    }
}
