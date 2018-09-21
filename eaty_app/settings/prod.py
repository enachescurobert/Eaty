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


ALLOWED_HOSTS = ['eaty.ovh', 'www.eaty.ovh']


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

STATIC_ROOT = os.path.join(CORE_PATH, 'statics/')


try:
  from eaty_app.settings.local import *
except:
  pass