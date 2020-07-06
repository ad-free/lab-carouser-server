# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import City, Ward, District


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
	fields = ('name', 'order', 'status')
	list_display = ('name', 'lat', 'lon', 'order', 'status')
	search_fields = ('name',)
	ordering = ('name',)


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
	fields = ('name', 'order', 'status')
	list_display = ('name', 'lat', 'lon', 'order', 'status')
	search_fields = ('name',)
	ordering = ('name',)


@admin.register(Ward)
class WardAdmin(admin.ModelAdmin):
	fields = ('name', 'order', 'status')
	list_display = ('name', 'lat', 'lon', 'order', 'status')
	search_fields = ('name',)
	ordering = ('name',)
