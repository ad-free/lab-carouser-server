# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer

from apps.apis.serializers.api_user_list import UserListSerializer

from apps.apis.utils import APIAccessPermission
from apps.commons.utils import Commons, Status, API

from functools import partial

from apps.users.models import Users


class UserList(APIView):
	""" Get user list """
	
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated & partial(APIAccessPermission, API().get_api_name('user', 'list'))]
	renderer_classes = [JSONRenderer]
	
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.commons = Commons()
		self.status = Status()
		self.error_msg = ''
	
	def post(self, request):
		serializer = UserListSerializer(data=self.request.data)
		
		if serializer.is_valid():
			page = serializer.data['page']
			obj_friends = Users.objects.distinct().all()\
				.values('id', 'first_name', 'last_name', 'email', 'sex', 'city__id', 'social_network')\
				.exclude(is_superuser=True)\
				.exclude(id=self.request.user.id)\
				.order_by('first_name', 'last_name')

			data = self.commons.paginator(obj=obj_friends, page=page, data_on_page=30)
			return self.commons.response(
				_status=self.status.HTTP_2000_OK,
				data={
					'users': data.object_list,
					'page': data.number
				}
			)
		else:
			self.error_msg = serializer.errors
		
		return self.commons.response(
			_status=self.status.HTTP_4000_BAD_REQUEST,
			error_msg=self.error_msg
		)
