# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import transaction
from django.utils.translation import ugettext_lazy as _

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.viewsets import ViewSet

from apps.apis.serializers.api_friend_list import FriendListSerializer

from apps.apis.utils import APIAccessPermission
from apps.commons.utils import Commons, Status, API

from functools import partial


class FriendList(ViewSet):
	""" Get friend list """
	
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated & partial(APIAccessPermission, API().get_api_name('friend', 'list'))]
	renderer_classes = [JSONRenderer]
	serializer_class = FriendListSerializer

	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.commons = Commons()
		self.status = Status()
		self.error_msg = _('Something wrong. Please try again.')
	
	@transaction.atomic()
	def create(self, request):
		serializer = self.serializer_class(data=request.data)
		
		if serializer.is_valid():
			page = serializer.data['page']
			obj_friends = request.user.friend.all()\
				.values(
				'id', 'first_name', 'last_name', 'email', 'sex',
				'social_network__facebook', 'social_network__twitter',
				'social_network__github', 'social_network__instagram'
			).order_by('first_name', 'last_name')
			data = self.commons.paginator(obj_friends, page, data_on_page=30)
			return self.commons.response(
				_status=self.status.HTTP_2000_OK,
				data={
					'friends': data.object_list,
					'page': data.number
				}
			)
		else:
			self.error_msg = serializer.errors
		
		return self.commons.response(
			_status=self.status.HTTP_4000_BAD_REQUEST,
			error_msg=self.error_msg
		)
