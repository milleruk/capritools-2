# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-13 01:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capritools2', '0044_auto_20170613_0103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fleet_member',
            name='key',
        ),
        migrations.AddField(
            model_name='fleet',
            name='key',
            field=models.CharField(default='asd', max_length=7),
            preserve_default=False,
        ),
    ]