# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
<<<<<<< HEAD
<<<<<<< HEAD
from rest_framework.renderers import JSONRenderer
from rest_framework.viewsets import ViewSet
=======
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
>>>>>>> e164e79... Update and optimize
=======
from rest_framework.renderers import JSONRenderer
from rest_framework.viewsets import ViewSet
>>>>>>> 40ba4e0... Update README.md

from apps.location.models import City

from apps.apis.serializers.api_city_list import CityListSerializer
<<<<<<< HEAD
<<<<<<< HEAD
=======

>>>>>>> e164e79... Update and optimize
=======
>>>>>>> 40ba4e0... Update README.md
from apps.apis.utils import APIAccessPermission
from apps.commons.utils import Commons, Status, API

from functools import partial


<<<<<<< HEAD
<<<<<<< HEAD
class CityList(ViewSet):
=======
class CityList(APIView):
>>>>>>> e164e79... Update and optimize
=======
class CityList(ViewSet):
>>>>>>> 40ba4e0... Update README.md
	""" Get city list """
	
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated & partial(APIAccessPermission, API().get_api_name('city', 'list'))]
	renderer_classes = [JSONRenderer]
<<<<<<< HEAD
<<<<<<< HEAD
	serializer_class = CityListSerializer
=======
>>>>>>> e164e79... Update and optimize
=======
	serializer_class = CityListSerializer
>>>>>>> 40ba4e0... Update README.md
	
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.commons = Commons()
		self.status = Status()
		self.error_msg = ''
<<<<<<< HEAD
<<<<<<< HEAD
		
	def create(self, request):
		self.commons.active_language(language=request.META.get('HTTP_LANGUAGE', getattr(settings, 'LANGUAGE_CODE')))
		serializer = self.serializer_class(data=self.request.data)
=======
	
	def post(self, request):
		self.commons.active_language(language=request.META.get('HTTP_LANGUAGE', getattr(settings, 'LANGUAGE_CODE')))
		serializer = CityListSerializer(data=self.request.data)
>>>>>>> e164e79... Update and optimize
=======
		
	def create(self, request):
		self.commons.active_language(language=request.META.get('HTTP_LANGUAGE', getattr(settings, 'LANGUAGE_CODE')))
		serializer = self.serializer_class(data=self.request.data)
>>>>>>> 40ba4e0... Update README.md
		
		if serializer.is_valid():
			page = serializer.data['page']
			obj_city_list = City.objects.distinct().filter(status=True)\
				.values('id', 'name')\
				.order_by('order', 'name')
			paginator = Paginator(obj_city_list, 30)
			try:
				data_each_page = paginator.page(page)
			except PageNotAnInteger:
				data_each_page = paginator.page(1)
			except EmptyPage:
				data_each_page = paginator.page(paginator.num_pages)
			data = {
				'city_list': data_each_page.object_list,
				'page': data_each_page.number
			}
			return self.commons.response(_status=self.status.HTTP_2000_OK, data=data)
		else:
			self.error_msg = serializer.errors
		return self.commons.response(_status=self.status.HTTP_4000_BAD_REQUEST, error_msg=self.error_msg)
