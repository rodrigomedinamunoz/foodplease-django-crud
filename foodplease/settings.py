from pathlib import Path
import os
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY - usar variable de entorno en producción
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-tu-key-actual')

# DEBUG
DEBUG = os.environ.get('DEBUG', 'True') == 'True'

# ALLOWED_HOSTS
ALLOWED_HOSTS = ['*']

# Database
DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///db.sqlite3',
        conn_max_age=600
    )
}

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Whitenoise - busca MIDDLEWARE y agrega justo después de SecurityMiddleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # <-- AGREGAR ESTA LÍNEA
    # ... resto del middleware
]


