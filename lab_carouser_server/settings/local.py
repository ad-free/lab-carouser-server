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
		# 'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
		'rest_framework.authentication.BasicAuthentication',
		'rest_framework.authentication.TokenAuthentication'
	),
	'DEFAULT_PERMISSION_CLASSES': (
		'rest_framework.permissions.IsAuthenticated',
	),
	'EXCEPTION_HANDLER': 'apps.commons.utils.custom_exception_handler'
}

JWT_AUTH = {
	'JWT_ENCODE_HANDLER':
		'rest_framework_jwt.utils.jwt_encode_handler',
	
	'JWT_DECODE_HANDLER':
		'rest_framework_jwt.utils.jwt_decode_handler',
	
	'JWT_PAYLOAD_HANDLER':
		'rest_framework_jwt.utils.jwt_payload_handler',
	
	'JWT_PAYLOAD_GET_USER_ID_HANDLER':
		'rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler',
	
	'JWT_RESPONSE_PAYLOAD_HANDLER':
		'rest_framework_jwt.utils.jwt_response_payload_handler',
	
	'JWT_SECRET_KEY': settings.SECRET_KEY,
	'JWT_GET_USER_SECRET_KEY': None,
	'JWT_PUBLIC_KEY': None,  # RS256, RS384, or RS512
	'JWT_PRIVATE_KEY': None,  # RS256, RS384, or RS512
	'JWT_ALGORITHM': 'HS256',
	'JWT_VERIFY': True,
	'JWT_VERIFY_EXPIRATION': True,
	'JWT_LEEWAY': 0,
	'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=60),
	'JWT_AUDIENCE': None,
	'JWT_ISSUER': None,
	
	'JWT_ALLOW_REFRESH': False,
	'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),
	
	'JWT_AUTH_HEADER_PREFIX': 'Token',
	'JWT_AUTH_COOKIE': None,
}

prod_db = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(prod_db)

# DATABASES = {
# 	'default': {
# 		'ENGINE': 'django.db.backends.mysql',
# 		'NAME': env.str('DB_NAME', None),
# 		'USER': env.str('DB_USER', None),
# 		'PASSWORD': env.str('DB_PASSWORD', None),
# 		'HOST': env.str('DB_HOST', None),
# 		'PORT': env.int('DB_PORT', None),
# 	}
# }

CACHE_TTL = 60  # seconds

CACHES = {
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
