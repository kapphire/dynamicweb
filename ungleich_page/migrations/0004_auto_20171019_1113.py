# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-10-19 11:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ungleich_page', '0003_auto_20171019_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sectionwithimage',
            name='menu_text',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='sectionwithimage',
            name='price_tag_url',
            field=models.URLField(blank=True, default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='service',
            name='menu_text',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='ungelichcontactussection',
            name='menu_text',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='ungelichtextsection',
            name='menu_text',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
