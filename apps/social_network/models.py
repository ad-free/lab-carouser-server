# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class SocialNetwork(models.Model):
	name = models.CharField(max_length=50)
	facebook = models.CharField(max_length=100, blank=True)
	twitter = models.CharField(max_length=100, blank=True)
	github = models.CharField(max_length=100, blank=True)
	instagram = models.CharField(max_length=100, blank=True)

	def __str__(self):
		return '{}'.format(self.name)

	def __unicode__(self):
		return u'{}'.format(self.name)
	
	class Meta:
		db_table = ''
		managed = True
		verbose_name = 'SocialNetwork'
		verbose_name_plural = 'SocialNetworks'
