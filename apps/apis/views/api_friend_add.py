# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.viewsets import ViewSet

from apps.users.models import Friend, Users

from apps.apis.serializers.api_friend_add import AddFriendSerializer
from apps.apis.utils import APIAccessPermission
from apps.commons.utils import Commons, Status, API

from functools import partial

<<<<<<< HEAD
<<<<<<< HEAD
=======
from apps.users.models import Friend, Users

>>>>>>> e164e79... Update and optimize
=======
>>>>>>> 40ba4e0... Update README.md

class AddFriend(ViewSet):
	""" Add a new friend """
	
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated & partial(APIAccessPermission, API().get_api_name('friend', 'add'))]
	renderer_classes = [JSONRenderer]
	serializer_class = AddFriendSerializer

	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.commons = Commons()
		self.status = Status()
		self.error_msg = _('Something wrong. Please try again.')
	
	def create(self, request):
		self.commons.active_language(language=request.META.get('HTTP_LANGUAGE', getattr(settings, 'LANGUAGE_CODE')))
		serializer = self.serializer_class(data=request.data)
		
		if serializer.is_valid(raise_exception=True):
			try:
				obj_user = Users.objects.get(id=serializer.data['user_id'])
				obj_friend, created = Friend.objects.update_or_create(
					id=obj_user.id,
					first_name=obj_user.first_name,
					last_name=obj_user.last_name,
					sex=obj_user.sex,
					email=obj_user.email,
					social_network=obj_user.social_network,
					city=obj_user.city
				)
<<<<<<< HEAD
<<<<<<< HEAD
				request.user.friend.add(obj_friend)
=======
				self.request.user.friend.add(obj_friend)
>>>>>>> e164e79... Update and optimize
=======
				request.user.friend.add(obj_friend)
>>>>>>> 40ba4e0... Update README.md
				return self.commons.response(
					_status=self.status.HTTP_2000_OK,
					message=_('You have successfully sent a friend request.')
				)
			except Users.DoesNotExist as e:
				self.commons.logs(level=2, message=str(e), name=__name__)
				self.error_msg = _('The user does not exists.')
			except Exception as e:
				self.commons.logs(level=3, message=str(e), name=__name__)
		else:
			self.error_msg = serializer.errors
		return self.commons.response(
			_status=self.status.HTTP_4000_BAD_REQUEST,
			error_msg=self.error_msg
		)
