from .common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-09$^3526099-7d25k*j!c9r6i^c45j9+19^kss3c$t_o1q3-e!'


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
# _psycopg2

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'backends',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'Agtm2486'

    }
}
