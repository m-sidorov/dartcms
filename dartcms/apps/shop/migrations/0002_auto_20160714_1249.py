# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-14 12:49
from __future__ import unicode_literals

import autoslug.fields
import dartcms.utils.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductManufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('description', dartcms.utils.fields.RteField(blank=True, default=b'', verbose_name='Description')),
                ('seo_keywords', models.TextField(blank=True, default=b'', verbose_name='Keywords (meta keywords)')),
                ('seo_description', models.TextField(blank=True, default=b'', verbose_name='Keywords (meta keywords)')),
                ('is_visible', models.BooleanField(default=True, verbose_name='Is Visible')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from=b'name', unique=True, verbose_name='URL')),
                ('image', models.ImageField(blank=True, null=True, upload_to=b'shop/producer', verbose_name='Image')),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
                'verbose_name': 'product manufacturer',
                'verbose_name_plural': 'product manufacturers',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='manufacturer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='manufacturer_products', to='shop.ProductManufacturer', verbose_name='Section'),
        ),
    ]