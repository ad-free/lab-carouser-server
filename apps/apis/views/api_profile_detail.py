# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.viewsets import ViewSet

from apps.apis.utils import APIAccessPermission
from apps.commons.utils import Commons, Status, API

from functools import partial


class ProfileDetail(ViewSet):
	""" Get profile detail """

	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated & partial(APIAccessPermission, API().get_api_name('profile', 'detail'))]
	renderer_classes = [JSONRenderer]
	
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.commons = Commons()
		self.status = Status()
		self.message = ''
		self.error_msg = _('Something wrong. Please try again.')
	
	def create(self, request):
		self.commons.active_language(language=request.META.get('HTTP_LANGUAGE', getattr(settings, 'LANGUAGE_CODE')))
		obj_user = self.request.user
		data = {
			'first_name': obj_user.first_name,
			'last_name': obj_user.last_name,
			'email': obj_user.email,
			'sex': obj_user.sex,
			'relationship_status': obj_user.relationship_status,
			'last_login': obj_user.last_login if obj_user.last_login else '',
			'date_joined': obj_user.date_joined,
			'is_update': obj_user.is_update,
			'city': obj_user.city_id,
			'facebook': obj_user.social_network.facebook if obj_user.social_network else '',
			'twitter': obj_user.social_network.twitter if obj_user.social_network else '',
			'instagram': obj_user.social_network.instagram if obj_user.social_network else '',
			'github': obj_user.social_network.github if obj_user.social_network else '',
		}
		return self.commons.response(_status=self.status.HTTP_2000_OK, data=data)
