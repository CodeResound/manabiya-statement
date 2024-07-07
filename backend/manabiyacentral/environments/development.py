import os
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()

SECRET_KEY = 'django-insecure-*&2l44(-(ir*d*#%bu#*3@u1m&84fpx!yc-h^zs2t@f6xk^3^v'

DEBUG = True

ALLOWED_HOSTS = ['*']


INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
    'authenticate'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.MultiPartParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.FileUploadParser'
    ],
    'UNAUTHENTICATED_USER': None,
    'EXCEPTION_HANDLER' : 'manabiyacentral.handlers.errorHandler.exceptions.custom_exception_handler',
}


ROOT_URLCONF = 'manabiyacentral.urls'

TEMPLATES = [
    
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'manabiya',
        'USER' : 'root',
        'PASSWORD' : 'Bitpassword47487@$',
        'HOST' : 'localhost',
        'PORT' : '3306',
    },
}

WSGI_APPLICATION = 'manabiyacentral.wsgi.application'


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



