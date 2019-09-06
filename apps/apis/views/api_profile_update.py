# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.db import transaction
from django.db import IntegrityError

from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer

from apps.location.models import Address

from apps.apis.serializers.api_profile_update import ProfileUpdateSerializer

from apps.apis.utils import APIAccessPermission
from apps.commons.utils import Commons, Status, API

from functools import partial


class ProfileUpdate(APIView):
	""" Update profile """
	
	authentication_classes = [JSONWebTokenAuthentication]
	permission_classes = [IsAuthenticated & partial(APIAccessPermission, API().get_api_name('profile', 'update'))]
	renderer_classes = [JSONRenderer]
	
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.status = Status()
		self.commons = Commons()
		self.error_msg = _('Something wrong. Please try again.')
		self.message = ''
	
	@transaction.atomic()
	def post(self, request):
		self.commons.active_language(language=request.META.get('HTTP_LANGUAGE', getattr(settings, 'LANGUAGE_CODE')))
		serializer = ProfileUpdateSerializer(data=self.request.data)
		if serializer.is_valid():
			self.error_msg = ''
			obj_user = self.request.user
			obj_user.first_name = serializer.data['first_name']
			obj_user.last_name = serializer.data['last_name']
			obj_user.sex = serializer.data['sex']
			obj_user.email = serializer.data['email']
			obj_user.relationship_status = serializer.data['relationship_status']
			obj_user.save()
			
			if ('city_id' and 'district_id' and 'ward_id') in serializer.data:
				try:
					with transaction.atomic():
						Address.objects.select_related('ward__district__city').update_or_create(
							user=obj_user,
							city_id=serializer.data['city_id'],
							district_id=serializer.data['district_id'],
							ward_id=serializer.data['ward_id']
						)
				except IntegrityError as e:
					self.error_msg = _('Please check your address.')
					self.commons.logs(level=3, message=str(e), name=__name__)
			return self.commons.response(_status=self.status.HTTP_2000_OK, message=_('Update successful.'), error_msg=self.error_msg)
		else:
			self.error_msg = serializer.errors
		return self.commons.response(_status=self.status.HTTP_4000_BAD_REQUEST, error_msg=self.error_msg)
