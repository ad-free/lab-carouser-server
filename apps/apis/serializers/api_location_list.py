# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers


class LocationListSerializer(serializers.Serializer):
	city_id = serializers.UUIDField(required=False)
	district_id = serializers.UUIDField(required=False)
	ward_id = serializers.UUIDField(required=False)
	page = serializers.CharField(max_length=6, default=1)
	
	def create(self, validated_data):
		pass
	
	def update(self, instance, validated_data):
		pass
