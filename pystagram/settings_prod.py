from .settings import *  # noqa
import os


if 'X_SECRET_KEY' in os.environ:
    SECRET_KEY = os.environ['X_SECRET_KEY']

DEBUG = False
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pystagram1_db',
        'USER': 'ubuntu1',
        'PASSWORD': 'mypassword1',
        'HOST': '127.0.0.1',
    },
}