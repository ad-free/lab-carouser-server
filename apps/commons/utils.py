# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils import translation
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from rest_framework.authtoken.models import Token
from rest_framework_jwt.settings import api_settings
from rest_framework.views import Response, exception_handler

import logging


def custom_exception_handler(exc, context):
	response = exception_handler(exc, context)
	commons = Commons()
	
	if response is not None:
		commons.logs(level=3, message=response.data['detail'], name=context['view'])
		response = commons.response(_status=commons.status.HTTP_4001_UNAUTHORIZED, error_msg=response.data['detail'])
	
	return response


class Commons:
	
	def __init__(self):
		self.logging = logging.getLogger()
		self.status = Status()
		self.jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
		self.jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
		self.jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
	
	def active_language(self, language):
		try:
			translation.activate(language)
			return True
		except Exception as e:
			self.logs(level=3, message=str(e), name=__name__)
		return False
	
	def response(self, _status=None, data=None, message=None, error_msg=None):
		return Response({
			'status_code': _status if _status else self.status.HTTP_4000_BAD_REQUEST,
			'result': True if _status == self.status.HTTP_2000_OK else False,
			'data': [data] if data else [],
			'message': message if message else '',
			'errors': [error_msg] if error_msg else []
		}, status=200)
	
	def logs(self, level=99, message='', name=''):
		""" Storage log here """
		msg = '{} [{}]'.format(name, message)
		if level == 0:
			return message
		if level == 1:
			return self.logging.info(msg)
		elif level == 2:
			return self.logging.warning(msg)
		elif level == 3:
			return self.logging.error(msg)
		else:
			return self.logging.critical(msg)
	
	def init_token(self, obj_user):
		try:
			# self.jwt_decode_handler(token)
			token = obj_user.auth_token.key
		except Exception as e:
			self.logs(level=1, message='{} {}'.format(obj_user.username, str(e)), name=__name__)
			# payload = self.jwt_payload_handler(obj_user)
			# token = self.jwt_encode_handler(payload)
			token = Token.objects.create(user=obj_user)
			token = token.key
		# cache.set(obj_user.username, token, getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT))
		return token
	
	@classmethod
	def paginator(cls, obj, page=1, data_on_page=30):
		paginator = Paginator(obj, data_on_page)
		try:
			data_each_page = paginator.page(page)
		except PageNotAnInteger:
			data_each_page = paginator.page(1)
		except EmptyPage:
			data_each_page = paginator.page(paginator.num_pages)
		return data_each_page


class Status:
	""" Init error code """
	
	def __init__(self):
		self.HTTP_1000_CONTINUE = 1000
		self.HTTP_1001_SWITCHING_PROTOCOLS = 1001
		self.HTTP_2000_OK = 2000
		self.HTTP_2001_CREATED = 2001
		self.HTTP_2002_ACCEPTED = 2002
		self.HTTP_2003_NON_AUTHORITATIVE_INFORMATION = 2003
		self.HTTP_2004_NO_CONTENT = 2004
		self.HTTP_2005_RESET_CONTENT = 2005
		self.HTTP_2006_PARTIAL_CONTENT = 2006
		self.HTTP_2007_MULTI_STATUS = 2007
		self.HTTP_2008_ALREADY_REPORTED = 2008
		self.HTTP_2026_IM_USED = 2026
		self.HTTP_3000_MULTIPLE_CHOICES = 3000
		self.HTTP_3001_MOVED_PERMANENTLY = 3001
		self.HTTP_3002_FOUND = 3002
		self.HTTP_3003_SEE_OTHER = 3003
		self.HTTP_3004_NOT_MODIFIED = 3004
		self.HTTP_3005_USE_PROXY = 3005
		self.HTTP_3006_RESERVED = 3006
		self.HTTP_3007_TEMPORARY_REDIRECT = 3007
		self.HTTP_3008_PERMANENT_REDIRECT = 3008
		self.HTTP_4000_BAD_REQUEST = 4000
		self.HTTP_4001_UNAUTHORIZED = 4001
		self.HTTP_4002_PAYMENT_REQUIRED = 4002
		self.HTTP_4003_FORBIDDEN = 4003
		self.HTTP_4004_NOT_FOUND = 4004
		self.HTTP_4005_METHOD_NOT_ALLOWED = 4005
		self.HTTP_4006_NOT_ACCEPTABLE = 4006
		self.HTTP_4007_PROXY_AUTHENTICATION_REQUIRED = 4007
		self.HTTP_4008_REQUEST_TIMEOUT = 4008
		self.HTTP_4009_CONFLICT = 4009
		self.HTTP_4010_GONE = 4010
		self.HTTP_4011_LENGTH_REQUIRED = 4011
		self.HTTP_4012_PRECONDITION_FAILED = 4012
		self.HTTP_4013_REQUEST_ENTITY_TOO_LARGE = 4013
		self.HTTP_4014_REQUEST_URI_TOO_LONG = 4014
		self.HTTP_4015_UNSUPPORTED_MEDIA_TYPE = 4015
		self.HTTP_4016_REQUESTED_RANGE_NOT_SATISFIABLE = 4016
		self.HTTP_4017_EXPECTATION_FAILED = 4017
		self.HTTP_4022_UNPROCESSABLE_ENTITY = 4022
		self.HTTP_4023_LOCKED = 4023
		self.HTTP_4024_FAILED_DEPENDENCY = 4024
		self.HTTP_4026_UPGRADE_REQUIRED = 4026
		self.HTTP_4028_PRECONDITION_REQUIRED = 4028
		self.HTTP_4029_TOO_MANY_REQUESTS = 4029
		self.HTTP_4031_REQUEST_HEADER_FIELDS_TOO_LARGE = 4031
		self.HTTP_4051_UNAVAILABLE_FOR_LEGAL_REASONS = 4051
		self.HTTP_5000_INTERNAL_SERVER_ERROR = 5000
		self.HTTP_5001_NOT_IMPLEMENTED = 5001
		self.HTTP_5002_BAD_GATEWAY = 5002
		self.HTTP_5003_SERVICE_UNAVAILABLE = 5003
		self.HTTP_5004_GATEWAY_TIMEOUT = 5004
		self.HTTP_5005_HTTP_VERSION_NOT_SUPPORTED = 5005
		self.HTTP_5006_VARIANT_ALSO_NEGOTIATES = 5006
		self.HTTP_5007_INSUFFICIENT_STORAGE = 5007
		self.HTTP_5008_LOOP_DETECTED = 5008
		self.HTTP_5009_BANDWIDTH_LIMIT_EXCEEDED = 5009
		self.HTTP_5010_NOT_EXTENDED = 5010
		self.HTTP_5011_NETWORK_AUTHENTICATION_REQUIRED = 5011


class API:
	""" Manage multiple api name """
	
	def __init__(self):
		pass
	
	@classmethod
	def get_api_name(cls, api_type='', api_name=''):
		""" :return API name """
		apis = {
			'auth': {
				'login': 'api_auth_login',
				'logout': 'api_auth_logout',
				'register': 'api_auth_register',
			},
			'profile': {
				'detail': 'api_profile_detail',
				'update': 'api_profile_update',
			},
			'friend': {
				'add': 'api_friend_add',
				'remove': 'api_friend_remove',
				'list': 'api_friend_list',
				'anonymous': 'api_friend_anonymous',
				'accept': 'api_friend_accept',
				'accept_list': 'api_friend_accept_list',
			},
			'location': {
				'list': 'api_location_list',
			},
			'': {
				'': 'Nothing here!'
			}
		}
		
		return apis.get(api_type, '').get(api_name, '')
