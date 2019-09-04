# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from .models import Friend, Staff, Users


@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
	fieldsets = (
		('Personal info', {
			'fields': ('first_name', 'last_name', 'phone_number', 'email', 'sex', 'avatar'),
		}),
	)
	list_display = ('email', 'first_name', 'last_name', 'phone_number', 'sex', 'created_at', 'updated_at')
	date_hierarchy = 'created_at'
	search_fields = ('email', 'first_name', 'last_name', 'phone_number',)
	list_filter = ('sex',)


@admin.register(Users)
class UsersAdmin(UserAdmin):
	fieldsets = (
		(None, {'fields': ('username', 'password')}),
		(_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'sex', 'relationship_status')}),
	)
	list_display = ('username', 'email', 'first_name', 'last_name', 'sex', 'relationship_status', 'last_login',)
	list_filter = ['date_joined', 'sex', 'relationship_status']
	exclude = ('groups',)
	readonly_fields = ('is_online',)
	date_hierarchy = 'date_joined'
	ordering = ('username',)
	
	def get_queryset(self, request):
		qs = super(UsersAdmin, self).get_queryset(request)
		return qs.filter(is_staff=False, is_superuser=False)
	
	def save_model(self, request, obj, form, change):
		obj.is_staff = False
		obj.is_superuser = False
		obj.save()


@admin.register(Staff)
class StaffAdmin(UserAdmin):
	fieldsets = (
		(None, {'fields': ('username', 'password')}),
		(_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
		(_('Permissions'), {'fields': ('is_active', 'is_superuser', 'groups')}),
	)
	list_display = ('username', 'first_name', 'email', 'is_active', 'last_login')
	list_filter = ['is_active', 'date_joined', 'last_login']
	filter_horizontal = ('groups',)
	exclude = ('user_permissions',)
	
	def get_queryset(self, request):
		qs = super(StaffAdmin, self).get_queryset(request)
		return qs.filter(is_staff=True)
	
	def save_model(self, request, obj, form, change):
		obj.is_staff = True
