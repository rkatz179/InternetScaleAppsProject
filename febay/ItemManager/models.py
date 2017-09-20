# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from UserManager.models import customer

# Create your models here.
class Item(models.Model):
    owner = models.ForeignKey(customer)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    price = models.FloatField()
    category = models.CharField(max_length=50)
    date_posted = models.DateTimeField()