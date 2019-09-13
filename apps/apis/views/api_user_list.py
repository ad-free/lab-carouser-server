# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.viewsets import ViewSet

<<<<<<< HEAD
<<<<<<< HEAD:apps/apis/views/api_user_list.py
from apps.users.models import Users
=======
from apps.apis.serializers.api_user_list import UserListSerializer
>>>>>>> e164e79... Update and optimize:apps/apis/views/api_friend_anonymous.py
=======
from apps.users.models import Users
>>>>>>> 40ba4e0... Update README.md

from apps.apis.serializers.api_user_list import UserListSerializer
from apps.apis.utils import APIAccessPermission
from apps.commons.utils import Commons, Status, API

from functools import partial

<<<<<<< HEAD
<<<<<<< HEAD:apps/apis/views/api_user_list.py

class UserList(ViewSet):
	""" Get user list """
=======
from apps.users.models import Users


class UserList(APIView):
	""" Update profile """
>>>>>>> e164e79... Update and optimize:apps/apis/views/api_friend_anonymous.py
=======

class UserList(ViewSet):
	""" Get user list """
>>>>>>> 40ba4e0... Update README.md
	
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated & partial(APIAccessPermission, API().get_api_name('user', 'list'))]
	renderer_classes = [JSONRenderer]
	serializer_class = UserListSerializer
	
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.commons = Commons()
		self.status = Status()
		self.error_msg = ''
	
<<<<<<< HEAD
<<<<<<< HEAD:apps/apis/views/api_user_list.py
	def create(self, request):
		self.commons.active_language(language=request.META.get('HTTP_LANGUAGE', getattr(settings, 'LANGUAGE_CODE')))
		serializer = self.serializer_class(data=request.data)
		
		if serializer.is_valid():
			page = serializer.data['page']
			obj_friends = Users.objects.distinct().all() \
				.values('id', 'first_name', 'last_name', 'email', 'sex', 'city__id', 'social_network') \
				.exclude(is_superuser=True) \
				.exclude(id=request.user.id) \
=======
	def post(self, request):
		serializer = UserListSerializer(data=self.request.data)
		
		if serializer.is_valid():
			page = serializer.data['page']
			obj_friends = Users.objects.distinct().all()\
				.values('id', 'first_name', 'last_name', 'email', 'sex', 'city__id', 'social_network')\
				.exclude(is_superuser=True)\
				.exclude(id=self.request.user.id)\
>>>>>>> e164e79... Update and optimize:apps/apis/views/api_friend_anonymous.py
=======
	def create(self, request):
		self.commons.active_language(language=request.META.get('HTTP_LANGUAGE', getattr(settings, 'LANGUAGE_CODE')))
		serializer = self.serializer_class(data=request.data)
		
		if serializer.is_valid():
			page = serializer.data['page']
			obj_friends = Users.objects.distinct().all() \
				.values('id', 'first_name', 'last_name', 'email', 'sex', 'city__id', 'social_network') \
				.exclude(is_superuser=True) \
				.exclude(id=request.user.id) \
>>>>>>> 40ba4e0... Update README.md
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
