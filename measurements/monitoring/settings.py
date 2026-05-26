import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-sprint4-key'
DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'measurements',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('MEASUREMENTS_DB_NAME', 'measurements_db'),
        'USER': os.environ.get('MEASUREMENTS_DB_USER', 'postgres'),
        'PASSWORD': os.environ.get('MEASUREMENTS_DB_PASSWORD', 'password'),
        'HOST': os.environ.get('MEASUREMENTS_DB_HOST', '127.0.0.1'),
        'PORT': os.environ.get('MEASUREMENTS_DB_PORT', '5432'),
    }
}

VARIABLES_HOST = os.environ.get('VARIABLES_HOST', '172.31.15.6')
VARIABLES_PORT = os.environ.get('VARIABLES_PORT', '8080')
PATH_VAR = f"http://{VARIABLES_HOST}:{VARIABLES_PORT}"

PLACES_HOST = os.environ.get('PLACES_HOST', '172.31.14.154')
PLACES_PORT = os.environ.get('PLACES_PORT', '8080')
PATH_PLACES = f"http://{PLACES_HOST}:{PLACES_PORT}"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
ROOT_URLCONF = 'monitoring.urls'
