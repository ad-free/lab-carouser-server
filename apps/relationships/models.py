# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.users.models import Users, Friend


class Relationship(models.Model):
	is_accept = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now=True)
	user = models.ForeignKey(Users, related_name='%(class)s_user', on_delete=models.CASCADE)
	friend = models.ForeignKey(Friend, related_name='%(class)s_friend', on_delete=models.CASCADE)
	
	class Meta:
		unique_together = ('user', 'friend',)
	
	def __str__(self):
		return '{}-{}'.format(self.user.email, self.friend.email)
	
	def __unicode__(self):
		return u'{}-{}'.format(self.user.email, self.friend.email)
