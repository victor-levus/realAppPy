import os
import dj_database_url
from .common import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["levus-database.herokuapp.com"]

CSRF_TRUSTED_ORIGINS = ['https://levus-database.herokuapp.com',
                        'https://localhost:3000']

DATABASES = {
    'default': dj_database_url.config()
}
