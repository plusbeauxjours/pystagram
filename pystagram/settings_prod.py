from .settings import *  # noqa
import os


if 'X_SECRET_KEY' in os.environ:
    SECRET_KEY = os.environ['X_SECRET_KEY']

DEBUG = False
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pystagram2_db',
        'USER': 'ubuntu2',
        'PASSWORD': 'mypassword2',
        'HOST': '127.0.0.1',
    },
}