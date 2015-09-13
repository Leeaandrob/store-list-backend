# coding: utf-8
from .settings import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'storelist_db',
        'HOST': 'localhost',
        'USER': 'storelist',
        'PASSWORD': 'qwert741258',
    }
}


ADMINS = (
    (u'Tracking Report Group', 'leandrobar93@gmail.com'),
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        # Include the default Django email handler for errors
        # This is what you'd get without configuring logging at all.
        'mail_admins': {
            'class': 'django.utils.log.AdminEmailHandler',
            'level': 'ERROR',
            'include_html': True,
        },
        # Log to a text file that can be rotated by logrotate
        'logfile': {
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': '/home/webapps/storelist/shared/log/storelist.log'
        },
    },
    'loggers': {
        # Again, default Django configuration to email unhandled exceptions
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        # Might as well log any errors anywhere else in Django
        'django': {
            'handlers': ['logfile'],
            'level': 'ERROR',
            'propagate': False,
        },
        # Your own app - this assumes all your logger names start with "myapp."
        'melhormenu': {
            'handlers': ['logfile'],
            'level': 'WARNING',
            'propagate': False
        },
    },
}


EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'leandrobar93@gmail.com'
EMAIL_HOST_PASSWORD = 'qwert741258'
EMAIL_HOST = 'smtp.gmail.com'
