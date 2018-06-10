from .base import *

SECRET_KEY = 'zaima8wzpo3bca1q)^v3)%t)qa3u7-hmzw2pfipj*jjgnw(**3'
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.dirname(BASE_DIR), 'trip_db.sqlite3'),
    }
}
