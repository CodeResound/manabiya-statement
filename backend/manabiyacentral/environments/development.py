from dotenv import load_dotenv


load_dotenv()

SECRET_KEY = 'django-insecure-*&2l44(-(ir*d*#%bu#*3@u1m&84fpx!yc-h^zs2t@f6xk^3^v'

DEBUG = True

ALLOWED_HOSTS = ['*']


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

CORS_ORIGIN_ALLOW_ALL = True
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

SESSION_COOKIE_SECURE=False
SESSION_COOKIE_HTTPONLY=True
SESSION_COOKIE_SAMESITE='None'





