# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-06 08:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='feed',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='feed',
            name='slug',
        ),
    ]
