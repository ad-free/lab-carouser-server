# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import transaction
from django.utils.translation import ugettext_lazy as _

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer

from apps.apis.serializers.api_friend_accept import AcceptListSerializer

from apps.apis.utils import APIAccessPermission
from apps.commons.utils import Commons, Status, API

from functools import partial


class AcceptFriend(APIView):
	""" Update profile """
	
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated & partial(APIAccessPermission, API().get_api_name('friend', 'accept'))]
	renderer_classes = [JSONRenderer]
	
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.commons = Commons()
		self.status = Status()
		self.error_msg = _('Something wrong. Please try again.')
	
	@transaction.atomic()
	def post(self, request):
		serializer = AcceptListSerializer(data=self.request.data)
		
		if serializer.is_valid():
			try:
				with transaction.atomic():
					obj_friend = self.request.user.relationship_with.get(id=serializer.data['friend_id'])
					obj_friend.is_accept = True
					obj_friend.save()
			except Exception as e:
				self.commons.logs(level=2, message=str(e), name=__name__)
				self.error_msg = _('Friend does not exists.')
			else:
				return self.commons.response(
					_status=self.status.HTTP_2000_OK,
					message=_('Add new friend successful.')
				)
		else:
			self.error_msg = serializer.errors
		
		return self.commons.response(
			_status=self.status.HTTP_4000_BAD_REQUEST,
			error_msg=self.error_msg
		)
