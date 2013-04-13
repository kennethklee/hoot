from common import *

ENVIRONMENT = 'staging'
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'hoot',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'hoot',
        'PASSWORD': 'staging',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

MEDIA_ROOT = '/data/web/hoot.konquest.com/media'
STATIC_ROOT = '/data/web/hoot.konquest.com/static'

FABRIC_DOMAIN = 'hoot.konquest.com'
FABRIC_USER = 'deploy'
FABRIC_HOST = 'hoot.konquest.com'
FABRIC_PASSWORD = 'password123'
FABRIC_REPO = 'git@github.com:kennethklee/hoot.git'
FABRIC_BRANCH = 'master'
