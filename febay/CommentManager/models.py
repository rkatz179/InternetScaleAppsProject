# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from UserManager import models
from ItemManager import models

# Create your models here.

class Comment(models.Model):
	user = models.ForeignKey(UserManager.customer)
	item = models.ForeignKey(ItemManager.Item)
	message = models.CharField(max_length=200)
	date_posted = models.DateTimeField(default=timezone.now)