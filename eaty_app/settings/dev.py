"""
!!!!!!!!!!!!!!!!!!!!!!!!!!!!
IMPORTANT FOR NEXT DEVELOPER
!!!!!!!!!!!!!!!!!!!!!!!!!!!!

If you want to use dev.py instead of prod.py, use this command:

Windows:
export DJANGO_SETTINGS_MODULE=eaty_app.settings.dev

Linux(Ubuntu 16.04):
set DJANGO_SETTINGS_MODULE=eaty_app.settings.dev


"""

from eaty_app.settings.base import *

#Override base.py settings here

DEVELOP_PATH = (os.path.dirname(os.path.dirname(os.path.dirname(__file__))))


ALLOWED_HOSTS = ['*']

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            './templates',
            os.path.join(DEVELOP_PATH, 'statics',
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
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATICFILES_DIRS = [
    os.path.join(DEVELOP_PATH, "statics")
]

try:
  from eaty_app.settings.local import *
except:
  pass
