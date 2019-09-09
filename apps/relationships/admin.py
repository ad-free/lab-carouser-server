# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from apps.relationships.models import Relationship


@admin.register(Relationship)
class RelationshipAdmin(admin.ModelAdmin):
	fieldsets = (
		(None, {
			'fields': ('user', 'friend', 'is_accept'),
		}),
	)
	list_display = ('get_name_of_user', 'get_name_of_friend', 'created_at', 'is_accept',)
	list_filter = ('created_at', 'is_accept',)
	date_hierarchy = 'created_at'
	
	def get_name_of_user(self, obj):
		return '{} {}'.format(obj.user.first_name, obj.user.last_name)
	
	def get_name_of_friend(self, obj):
		return '{} {}'.format(obj.friend.first_name, obj.friend.last_name)
	
	get_name_of_user.admin_order_field = 'relationship'  # Allows column order sorting
	get_name_of_user.short_description = 'User'  # Renames column head
	get_name_of_friend.admin_order_field = 'relationship'  # Allows column order sorting
	get_name_of_friend.short_description = 'Friend'  # Renames column head
