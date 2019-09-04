# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings

from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.hashers import make_password

from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer

from apps.apis.utils import APIAccessPermission
from apps.users.models import Users

from apps.apis.serializers.api_register import RegisterSerializer

from apps.commons.utils import Commons, Status, API

from functools import partial


class Register(APIView):
	""" Register your account. """
	
	authentication_classes = []
	permission_classes = [partial(APIAccessPermission, API().get_api_name('auth', 'register'))]
	renderer_classes = [JSONRenderer]
	
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.status = Status()
		self.commons = Commons()
		self.error_msg = _('Something wrong. Please try again.')
		self.message = _('Congratulations. You have successfully registered.')
	
	def post(self, request):
		self.commons.active_language(language=request.META.get('HTTP_LANGUAGE', getattr(settings, 'LANGUAGE_CODE')))
		serializer = RegisterSerializer(data=self.request.data)
		if serializer.is_valid():
			if not serializer.compare_pwd(data=request.data):
				obj_user, created = Users.objects.get_or_create(username=serializer.data['username'], defaults={
					'password': make_password(serializer.data['password'])
				})
				
				if created:
					data = {
						'token': self.commons.init_token(obj_user)
					}
					self.commons.logs(level=1, message=str(obj_user) + ' has successfully registered.', name=self.__class__)
					return self.commons.response_format(_status=self.status.HTTP_2000_OK, data=data, message=self.message)
				self.error_msg = _('User always exists.')
			else:
				self.error_msg = _('Password does not match.')
		else:
			self.error_msg = serializer.errors
		
		self.commons.logs(level=2, message=self.error_msg, name=self.__class__)
		return self.commons.response_format(_status=self.status.HTTP_4000_BAD_REQUEST, error_msg=self.error_msg)
