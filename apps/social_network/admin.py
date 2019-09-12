# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import SocialNetwork


@admin.register(SocialNetwork)
class SocialNetwork(admin.ModelAdmin):
	fieldsets = (
		('Information', {
			'fields': ('name',)
		}),
		('Social Network', {
			'fields': ('facebook', 'twitter', 'github', 'instagram',)
		})
	)
	list_display = ('name', 'facebook', 'twitter', 'github', 'instagram',)
