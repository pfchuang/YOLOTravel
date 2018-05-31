from .base import *

SECRET_KEY = 'foo'
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.dirname(BASE_DIR), 'trip_db.sqlite3'),
    }
}
