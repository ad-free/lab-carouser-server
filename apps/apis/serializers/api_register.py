# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers


class RegisterSerializer(serializers.Serializer):
	username = serializers.CharField(max_length=30)
	password = serializers.CharField(max_length=255)
	confirm_password = serializers.CharField(max_length=255)
	
	@staticmethod
	def compare_pwd(data):
		if data['password'] != data['confirm_password']:
			return True
		return False
	
	def create(self, validated_data):
		pass
	
	def update(self, instance, validated_data):
		pass
