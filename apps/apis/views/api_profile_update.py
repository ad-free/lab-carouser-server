# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.db import transaction

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.viewsets import ViewSet

from apps.apis.serializers.api_profile_update import ProfileUpdateSerializer
from apps.apis.utils import APIAccessPermission
from apps.commons.utils import Commons, Status, API

from functools import partial


class ProfileUpdate(ViewSet):
	""" Update profile """
	
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated & partial(APIAccessPermission, API().get_api_name('profile', 'update'))]
	renderer_classes = [JSONRenderer]
	serializer_class = ProfileUpdateSerializer
	
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.status = Status()
		self.commons = Commons()
		self.message = ''
		self.error_msg = _('Something wrong. Please try again.')
	
	@transaction.atomic()
	def create(self, request):
		self.commons.active_language(language=request.META.get('HTTP_LANGUAGE', getattr(settings, 'LANGUAGE_CODE')))
		serializer = self.serializer_class(data=self.request.data)
		if serializer.is_valid():
			self.error_msg = ''
			obj_user = self.request.user
			obj_user.first_name = serializer.data['first_name']
			obj_user.last_name = serializer.data['last_name']
			obj_user.sex = serializer.data['sex']
			obj_user.email = serializer.data['email']
			obj_user.relationship_status = serializer.data['relationship_status']
			obj_user.city_id = serializer.data['city_id']
			obj_user.is_update = True
			obj_user.save()
			return self.commons.response(_status=self.status.HTTP_2000_OK, message=_('Update successful.'), error_msg=self.error_msg)
		else:
			self.error_msg = serializer.errors
		return self.commons.response(_status=self.status.HTTP_4000_BAD_REQUEST, error_msg=self.error_msg)
