# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers


class FriendListSerializer(serializers.Serializer):
	""" Get list friend """
	
	page = serializers.IntegerField(default=1)
	
	def create(self, validated_data):
		pass
	
	def update(self, instance, validated_data):
		pass
