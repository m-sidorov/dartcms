# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-06 06:54
from __future__ import unicode_literals

from django.db import migrations

from dartcms.utils.loading import get_model

PageModule = get_model('pages', 'PageModule')


def insert_module(apps, schema):
    PageModule.objects.create(slug='feedback', name='Feedback', related_model='feedback.FormType'),


def drop_module(apps, schema):
    PageModule.objects.get(slug='feedback').delete()


class Migration(migrations.Migration):
    dependencies = [
        ('pages', '0006_auto_20160711_1627'),
    ]

    operations = [
        migrations.RunPython(insert_module, drop_module)
    ]
