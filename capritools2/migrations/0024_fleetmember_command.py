# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-10 01:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capritools2', '0023_auto_20170610_0058'),
    ]

    operations = [
        migrations.AddField(
            model_name='fleetmember',
            name='command',
            field=models.BooleanField(default=False),
        ),
    ]