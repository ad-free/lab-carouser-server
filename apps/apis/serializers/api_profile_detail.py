# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers

from apps.users.models import SEX_OPTIONS, RELATIONSHIP_STATUS


class ProfileUpdateSerializer(serializers.Serializer):

	def create(self, validated_data):
		pass

	def update(self, instance, validated_data):
		pass
