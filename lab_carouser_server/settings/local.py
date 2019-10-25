# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .base import *
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

import dj_database_url
import datetime

DEBUG = True

INSTALLED_APPS += [
	'rest_framework.authtoken',
	'apps.apis',
	'apps.location',
	'apps.users',
	'apps.social_network',
]

TIME_ZONE = 'Asia/Ho_Chi_Minh'
USE_TZ = True
USE_I18N = True

LANGUAGES = (
	('en', _('English')),
	('vi', _('Vietnamese')),
)
LANGUAGE_CODE = 'en'

REST_FRAMEWORK = {
	'DEFAULT_AUTHENTICATION_CLASSES': (
		'rest_framework.authentication.BasicAuthentication',
		'rest_framework.authentication.TokenAuthentication'
	),
	'DEFAULT_PERMISSION_CLASSES': (
		'rest_framework.permissions.IsAuthenticated',
	),
	'EXCEPTION_HANDLER': 'apps.commons.utils.custom_exception_handler'
}

DATABASES = {
	'default': {
		'BACKEND': 'django_redis.cache.RedisCache',
		'LOCATION': 'redis://127.0.0.1:6379/',
		# 'TIMEOUT': 0,
		'OPTIONS': {
			'CLIENT_CLASS': 'django_redis.client.DefaultClient',
		},
	}
}

LOGGING = {
	'version': 1,
	'disable_existing_loggers': True,
	'formatters': {
		'verbose': {
			'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
			'datefmt': "%d/%b/%Y-%H:%M:%S"
		},
		'simple': {
			'format': '%(levelname)s %(message)s'
		},
	},
	'handlers': {
		'file': {
			'level': 'INFO',
			'class': 'logging.handlers.TimedRotatingFileHandler',
			'filename': os.path.join(settings.LOG_DIR, 'api.log'),
			'when': 'D',
			'interval': 1,
			'backupCount': 10,
			'formatter': 'verbose',
		},
	},
	'loggers': {
		'': {
			'handlers': ['file'],
			'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
		},
		'root': {
			'handlers': ['file'],
			'level': os.getenv('DJANGO_LOG_LEVEL', 'ERROR'),
		}
	},
}
