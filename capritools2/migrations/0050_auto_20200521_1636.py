# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-21 16:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capritools2', '0049_auto_20180530_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(null=True),
        ),
    ]