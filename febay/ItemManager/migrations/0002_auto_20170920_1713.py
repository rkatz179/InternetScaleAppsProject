# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-20 21:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ItemManager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]