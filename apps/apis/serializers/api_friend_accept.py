# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers


class AcceptListSerializer(serializers.Serializer):
	friend_id = serializers.UUIDField()
	
	def create(self, validated_data):
		pass
	
	def update(self, instance, validated_data):
		pass
