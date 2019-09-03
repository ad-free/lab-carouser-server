# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate, login


from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer

from apps.apis.serializers.api_login import LoginSerializer
from apps.apis.utils import APIAccessPermission

from apps.commons.utils import Commons, Status, API

from functools import partial


class Login(APIView):
	""" API Login """
	
	authentication_classes = []
	permission_classes = [partial(APIAccessPermission, API(api_type='auth', api_name='login').get_api_name())]
	renderer_classes = [JSONRenderer]
	
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.status = Status()
		self.commons = Commons()
		self.error_msg = _('Something wrong. Please try again.')
		self.message = _('You are successfully logged in.')
	
	def post(self, request):
		self.commons.active_language(language=request.META.get('HTTP_LANGUAGE', getattr(settings, 'LANGUAGE_CODE')))
		serializer = LoginSerializer(data=self.request.data)
		
		if serializer.is_valid():
			obj_user = authenticate(username=serializer.data['username'], password=serializer.data['password'])
			
			if obj_user is not None:
				login(request, obj_user)
				data = {
					'token': self.commons.init_token(obj_user)
				}
				
				self.commons.logs(level=1, message=str(obj_user) + ' has successfully logged in.', name=self.__class__)
				return self.commons.response_format(_status=self.status.HTTP_2000_OK, data=data, message=self.message)
			self.error_msg = _('User does not exists.')
		else:
			self.error_msg = serializer.errors
		
		self.commons.logs(level=2, message=self.error_msg, name=self.__class__)
		return self.commons.response_format(_status=self.status.HTTP_4000_BAD_REQUEST, error_msg=self.error_msg)
