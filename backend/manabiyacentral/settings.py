import os
from pathlib import Path
from dotenv import load_dotenv
from datetime import timedelta


load_dotenv()

ROOT_DIR = Path(__file__).resolve().parent.parent.parent
BACKEND_DIR = Path(__file__).resolve().parent.parent 
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOGS_DIR = os.path.join(ROOT_DIR, 'logs')
if not os.path.exists(LOGS_DIR):
    os.makedirs(LOGS_DIR)

MEDIA_DIR = os.path.join(ROOT_DIR,'media')
if not os.path.exists(MEDIA_DIR):
    os.makedirs(MEDIA_DIR)

ENVIRONMENT = os.getenv('ENVIRONMENT','development')

if ENVIRONMENT == 'production':
    from manabiyacentral.environments.production import *
else:
    from manabiyacentral.environments.development import *


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,  # Ensure this is set to True
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
            ],
        },
    },
]


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(asctime)s - %(filename)s : %(lineno)s - %(message)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(ROOT_DIR, 'logs/errors.log'),
            'maxBytes': 10 * 1024 * 1024,
            'backupCount': 10,
            'formatter': 'verbose',
            'encoding': 'utf-8',
        },
    },
    'root': { 
        'handlers': ['error'],
        'level': 'ERROR',
    },
}
