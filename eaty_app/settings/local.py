#Override base.py settings in prod.py/dev.py with this:

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'u0)gc+dh+f_u5_a_i*e2qdw9gw--t45d%v_-5q6lej8u#emuaw'

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


