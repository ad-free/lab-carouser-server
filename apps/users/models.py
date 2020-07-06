# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import EmailValidator

from apps.location.models import City
from apps.auth.models import User
from apps.social_network.models import SocialNetwork


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
	city = models.ForeignKey(City, related_name='%(class)s_city', on_delete=models.CASCADE)
	social_network = models.ForeignKey(SocialNetwork, related_name='%(class)s_social_network', on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	class Meta:
		verbose_name = 'Friend'
		verbose_name_plural = 'Friends'
	
	def __str__(self):
		return '{} {}'.format(self.first_name, self.last_name)

	def __unicode__(self):
		return u'{} {}'.format(self.first_name, self.last_name)


class Users(User):
	phone_number = models.CharField(max_length=100)
	avatar = models.FileField(blank=True, null=True, upload_to='avatar/%Y/%m/%d/')
	sex = models.SmallIntegerField(choices=SEX_OPTIONS, default=0)
	relationship_status = models.SmallIntegerField(choices=RELATIONSHIP_STATUS, default=0)
	is_online = models.BooleanField(default=False, verbose_name=_('Online'))
	is_update = models.BooleanField(default=False)
	city = models.ForeignKey(City, blank=True, null=True, related_name='%(class)s_city', on_delete=models.CASCADE)
	social_network = models.ForeignKey(SocialNetwork, blank=True, null=True, related_name='%(class)s_social_network', on_delete=models.CASCADE)
	friend = models.ManyToManyField(Friend, blank=True, related_name='%(class)s_friend')


	def __str__(self):
		return '{}'.format(self.username)
	
	def __unicode__(self):
		return u'{}'.format(self.username)
	
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
