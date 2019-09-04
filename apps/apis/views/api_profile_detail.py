# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer

from apps.location.models import Address

from apps.apis.utils import APIAccessPermission
from apps.commons.utils import Commons, Status, API

from functools import partial


class ProfileDetail(APIView):
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated & partial(APIAccessPermission, API().get_api_name('profile', 'detail'))]
	renderer_classes = [JSONRenderer]
	
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.commons = Commons()
		self.status = Status()
		self.error_msg = _('Something wrong. Please try again.')
		self.message = ''
		self.data = {
			'first_name': '',
			'last_name': '',
			'email': '',
			'sex': '',
			'relationship_status': '',
			'last_login': '',
			'date_joined': '',
			'city': '',
			'district': '',
			'ward': ''
		}
	
	def post(self, request):
		self.commons.active_language(language=request.META.get('HTTP_LANGUAGE', getattr(settings, 'LANGUAGE_CODE')))
		obj_user = self.request.user
		try:
			obj_address = Address.objects.get(user=obj_user)
			self.data.update({
				'city': obj_address.city__name,
				'district': obj_address.district__name,
				'ward': obj_address.ward__name
			})
		except Address.DoesNotExist:
			self.commons.logs(level=2, message='{} {}'.format(obj_user.username, _('Address does not exists.')), name=__name__)
		
		if obj_user:
			self.data.update({
				'first_name': obj_user.first_name,
				'last_name': obj_user.last_name,
				'email': obj_user.email,
				'sex': obj_user.sex,
				'relationship_status': obj_user.relationship_status,
				'last_login': obj_user.last_login if obj_user.last_login else '',
				'date_joined': obj_user.date_joined,
			})
			return self.commons.response_format(_status=self.status.HTTP_2000_OK, data=self.data)
		return self.commons.response_format(_status=self.status.HTTP_4000_BAD_REQUEST, error_msg=self.error_msg)
