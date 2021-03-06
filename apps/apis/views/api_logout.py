# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import logout

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.viewsets import ViewSet

from apps.apis.utils import APIAccessPermission
from apps.commons.utils import Commons, Status, API

from functools import partial
import base64


class Logout(ViewSet):
	""" Logout to system """
	
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated & partial(APIAccessPermission, API().get_api_name('auth', 'logout'))]
	renderer_classes = [JSONRenderer]
	
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.status = Status()
		self.commons = Commons()
		self.message = _('Logout successful.')
		self.error_msg = _('You must be login to system.')
	
	def create(self, request):
		self.commons.active_language(language=request.META.get('HTTP_LANGUAGE', getattr(settings, 'LANGUAGE_CODE')))
		try:
			self.request.user.auth_token.delete()
			logout(request)
			self.commons.logs(level=1, message=self.message, name=__name__)
			return self.commons.response(_status=self.status.HTTP_2000_OK, message=self.message)
		except Exception as e:
			self.error_msg = str(e)
			self.commons.logs(level=3, message=self.error_msg, name=__name__)
		
		self.commons.logs(level=2, message=self.error_msg, name=__name__)
		return self.commons.response(_status=self.status.HTTP_4000_BAD_REQUEST, error_msg=self.error_msg)
