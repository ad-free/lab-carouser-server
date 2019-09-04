# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.validators import EmailValidator

from rest_framework import serializers

from apps.users.models import SEX_OPTIONS, RELATIONSHIP_STATUS


class ProfileUpdateSerializer(serializers.Serializer):
	first_name = serializers.CharField(max_length=30)
	last_name = serializers.CharField(max_length=30)
	email = serializers.EmailField(validators=[EmailValidator])
	sex = serializers.ChoiceField(choices=SEX_OPTIONS, default=0)
	relationship_status = serializers.ChoiceField(choices=RELATIONSHIP_STATUS, default=0)
	city_id = serializers.UUIDField(required=False)
	district_id = serializers.UUIDField(required=False)
	ward_id = serializers.UUIDField(required=False)
	
	def create(self, validated_data):
		pass
	
	def update(self, instance, validated_data):
		pass
