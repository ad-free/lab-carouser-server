# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from ..users.models import Users

import uuid


class City(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
	name = models.CharField(max_length=150)
	lat = models.FloatField(blank=True, null=True)
	lon = models.FloatField(blank=True, null=True)
	order = models.PositiveIntegerField(default=1, verbose_name=_('Order number'))
	status = models.BooleanField(default=True)
	
	class Meta:
		verbose_name_plural = _('Cities')
	
	def __str__(self):
		return self.name
	
	def __unicode__(self):
		return self.name


class District(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
	name = models.CharField(max_length=150)
	city = models.ForeignKey(City, related_name='%(class)s_city', on_delete=models.CASCADE)
	lat = models.FloatField(blank=True, null=True)
	lon = models.FloatField(blank=True, null=True)
	order = models.PositiveIntegerField(default=1, verbose_name=_('Order number'))
	status = models.BooleanField(default=True)
	
	def __str__(self):
		return '{}-{}'.format(self.city, self.name)
	
	def __unicode__(self):
		return u'{}-{}'.format(self.city, self.name)


class Ward(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
	name = models.CharField(max_length=150)
	district = models.ForeignKey(District, related_name='%(class)s_district', on_delete=models.CASCADE)
	lat = models.FloatField(blank=True, null=True)
	lon = models.FloatField(blank=True, null=True)
	order = models.PositiveIntegerField(default=1, verbose_name=_('Order number'))
	status = models.BooleanField(default=True)
	
	def __str__(self):
		return '{}-{}'.format(self.district, self.name)
	
	def __unicode__(self):
		return u'{}-{}'.format(self.district, self.name)


class Address(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
	street_no = models.TextField(max_length=30)
	street_name = models.TextField(max_length=150)
	is_default = models.BooleanField(default=False)
	user = models.ForeignKey(Users, related_name='%(class)s_user', on_delete=models.CASCADE)
	city = models.ForeignKey(City, related_name='%(class)s_city', on_delete=models.CASCADE)
	district = models.ForeignKey(District, blank=True, related_name='%(class)s_district', on_delete=models.CASCADE)
	ward = models.ForeignKey(Ward, blank=True, related_name='%(class)s_ward', on_delete=models.CASCADE)
	
	class Meta:
		verbose_name = 'Address'
		verbose_name_plural = 'Addresses'
	
	def __str__(self):
		return '{}, {}, {}'.format(self.city, self.district.name, self.ward.name)
	
	def __unicode__(self):
		return u'{}, {}, {}'.format(self.city, self.district.name, self.ward.name)
