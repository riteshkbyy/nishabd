# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-23 05:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20160516_0137'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='description_truncated',
            field=models.TextField(blank=True, null=True),
        ),
    ]
