# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer

from apps.location.models import City, District, Ward

from apps.apis.serializers.api_location_list import LocationListSerializer

from apps.apis.utils import APIAccessPermission
from apps.commons.utils import Commons, Status, API

from functools import partial


class LocationList(APIView):
	""" Get city list """
	
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated and partial(APIAccessPermission, API().get_api_name('location', 'list'))]
	renderer_classes = [JSONRenderer]
	
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.commons = Commons()
		self.status = Status()
		self.obj_name = ['cities', 'districts', 'wards']
		self.obj_list = []
		self.error_msg = ''
	
	def post(self, request):
		self.commons.active_language(language=request.META.get('HTTP_LANGUAGE', getattr(settings, 'LANGUAGE_CODE')))
		serializer = LocationListSerializer(data=self.request.data)
		
		if serializer.is_valid():
			page = serializer.data['page']
			
			if 'city_id' in serializer.data and 'district_id' in serializer.data:
				self.obj_name = self.obj_name[2]
				self.obj_list = Ward.objects.prefetch_related('district')\
					.filter(district_id=serializer.data['district_id'], district__city__id=serializer.data['city_id'])\
					.values('id', 'name')\
					.order_by('order', 'name')
			elif 'city_id' in serializer.data:
				self.obj_name = self.obj_name[1]
				self.obj_list = District.objects.prefetch_related('city')\
					.filter(city_id=serializer.data['city_id'])\
					.values('id', 'name')\
					.order_by('order', 'name')
			else:
				self.obj_name = self.obj_name[0]
				self.obj_list = City.objects.distinct().filter(status=True).values('id', 'name').order_by('order', 'name')
				
			if not self.error_msg:
				paginator = Paginator(self.obj_list, 30)
				try:
					data_each_page = paginator.page(page)
				except PageNotAnInteger:
					data_each_page = paginator.page(1)
				except EmptyPage:
					data_each_page = paginator.page(paginator.num_pages)
				data = {
					self.obj_name: data_each_page.object_list,
					'page': data_each_page.number
				}
				return self.commons.response(_status=self.status.HTTP_2000_OK, data=data)
		else:
			self.error_msg = serializer.errors
		return self.commons.response(_status=self.status.HTTP_4000_BAD_REQUEST, error_msg=self.error_msg)
