# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import EmailValidator

from apps.auth.models import User

import uuid

RELATIONSHIP_STATUS = (
	(0, _('Single')),
	(1, _('In a relationship')),
	(2, _('Married')),
)

SEX_OPTIONS = (
	(0, _('Unknown')),
	(1, _('Male')),
	(2, _('Female')),
)


class Friend(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	phone_number = models.CharField(max_length=255, blank=True)
	email = models.EmailField(validators=[EmailValidator])
	sex = models.SmallIntegerField(choices=SEX_OPTIONS, default=0)
	avatar = models.FileField(blank=True, null=True, upload_to='avatar/%Y/%m/%d/')
	is_online = models.BooleanField(default=False, verbose_name=_('Online'))
	is_accept = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	class Meta:
		verbose_name = 'Friend'
		verbose_name_plural = 'Friends'
	
	def __str__(self):
		return '{} {}'.format(self.first_name, self.last_name)


class Users(User):
	avatar = models.FileField(blank=True, null=True, upload_to='avatar/%Y/%m/%d/')
	is_online = models.BooleanField(default=False, verbose_name=_('Online'))
	sex = models.SmallIntegerField(choices=SEX_OPTIONS, default=0)
	relationship_status = models.SmallIntegerField(choices=RELATIONSHIP_STATUS, default=0)
	is_update = models.BooleanField(default=False)
	relationship_with = models.ManyToManyField(Friend, blank=True, related_name='%(class)s_relationship_with')
	friend = models.ManyToManyField(Friend, blank=True, related_name='%(class)s_friend')
	
	class Meta:
		verbose_name = 'User'
		verbose_name_plural = 'Users'


class Staff(Users):
	def __str__(self):
		return self.username
	
	def __unicode__(self):
		return u'{}'.format(self.username)
	
	class Meta:
		proxy = True
		verbose_name = 'Staff'
		verbose_name_plural = 'Staffs'
