"""
!!!!!!!!!!!!!!!!!!!!!!!!!!!!
IMPORTANT FOR NEXT DEVELOPER
!!!!!!!!!!!!!!!!!!!!!!!!!!!!

If you want to use prod.py instead of dev.py in production(like you should), use this command:

Windows:
export DJANGO_SETTINGS_MODULE=eaty_app.settings.prod

Linux(Ubuntu 16.04):
set DJANGO_SETTINGS_MODULE=eaty_app.settings.prod


"""

from eaty_app.settings.base import *

#Override base.py settings here

PROD_PATH = (os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

DEBUG = False


ALLOWED_HOSTS = ['eaty.ovh', 'www.eaty.ovh']

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            './templates',
            os.path.join(PROD_PATH, 'statics',
            )

        ],
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


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': '0.0.0.0',
        'PORT': '5432',
    }
} 

STATIC_ROOT = os.path.join(PROD_PATH, 'statics/')


try:
  from eaty_app.settings.local import *
except:
  pass