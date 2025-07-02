from pathlib import Path
import os
import dj_database_url
import cloudinary

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Security
SECRET_KEY = 'django-insecure--l4=w@^ihb6r9t8l1mq9jjnx=86q5*d=*a^srrimj6&j4_4c*e'
DEBUG = True
ALLOWED_HOSTS = ['*']

# Cloudinary setup (required)
cloudinary.config(
    cloud_name="dh5jzme9e",
    api_key="882124884944959",
    api_secret="SwulHqaokKHOVa9tkEjcYYq-FVI"
)

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dh5jzme9e',
    'API_KEY': '882124884944959',
    'API_SECRET': 'SwulHqaokKHOVa9tkEjcYYq-FVI',
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# Installed apps
INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'webapp',
    'crispy_forms',
    'crispy_bootstrap5',
    'widget_tweaks',
    'cloudinary',
    'cloudinary_storage',
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URLs
ROOT_URLCONF = 'ecommerce.urls'

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI
WSGI_APPLICATION = 'ecommerce.wsgi.application'

# Database
DATABASES = {
    'default': dj_database_url.config(
        default='postgres://ecom_owner:npg_AkDvph0uJwP3@ep-bold-recipe-a8wabwbj-pooler.eastus2.azure.neon.tech/ecom?sslmode=require&channel_binding=require'
    )
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'webapp/static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
