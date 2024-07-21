import os
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = [
    os.getenv("ALLOWEDHOST1"),
    os.getenv("ALLOWEDHOST2"),
    os.getenv("ALLOWEDHOST3"),
    os.getenv("ALLOWEDHOST4"),
    os.getenv("ALLOWEDHOST5"),
    os.getenv("ALLOWEDHOST6"),
    os.getenv("ALLOWEDHOST7"),
    os.getenv("ALLOWEDHOST8"),
    os.getenv("ALLOWEDHOST9"),
]


INSTALLED_APPS = [
    'rest_framework',
    'corsheaders',
    'authenticate',
    'statements',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES':[
        'manabiyacentral.middlewares.auth_token.JWTAuthentication'
    ],
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
        'ENGINE': os.getenv('PROD_DB_ENGINE'),
        'NAME': os.getenv('PROD_DB_NAME'),
        'USER': os.getenv('PROD_DB_USER'),
        'PASSWORD': os.getenv('PROD_DB_PASSWORD'),
        'HOST': os.getenv('PROD_DB_HOST'),
        'PORT': os.getenv('PROD_DB_PORT'),
        'CONN_MAX_AGE': 600
    }
}

WSGI_APPLICATION = 'manabiyacentral.wsgi.application'


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


SESSION_COOKIE_HTTPONLY=True
CSRF_COOKIE_HTTPONLY=True
CSRF_COOKIE_SECURE=True
SESSION_COOKIE_SAMESITE='Strict'
CSRF_COOKIE_SAMESITE='Strict'
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = [
    os.getenv('ALLOWEDORIGIN1'),
    os.getenv('ALLOWEDORIGIN2'),
    os.getenv('ALLOWEDORIGIN3'),
    os.getenv('ALLOWEDORIGIN4'),
    os.getenv('ALLOWEDORIGIN5'),
    os.getenv('ALLOWEDORIGIN6'),
    os.getenv('ALLOWEDORIGIN7'),
    os.getenv('ALLOWEDORIGIN8'),
    os.getenv('ALLOWEDORIGIN9'),
]

CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'Authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'Set-Cookie',
    'X-Authorization'
]

CORS_ALLOW_METHODS = [
    'GET',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
    'OPTIONS',
]

CORS_EXPOSE_HEADERS = [
    'XAuthorization',
    'Authorization',
    'Set-Cookie',
]

SESSION_COOKIE_SECURE=True
SESSION_COOKIE_HTTPONLY=True
SESSION_COOKIE_SAMESITE='Strict'
CSRF_COOKIE_SECURE = True




