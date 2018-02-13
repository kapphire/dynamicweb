# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2018-01-05 12:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_auto_20160404_1908'),
        ('ungleich_page', '0017_auto_20171219_1856'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ungleichheader',
            name='background_image',
        ),
        migrations.RemoveField(
            model_name='ungleichheader',
            name='cmsplugin_ptr',
        ),
        migrations.RemoveField(
            model_name='ungleichheaderitem',
            name='cmsplugin_ptr',
        ),
        migrations.RemoveField(
            model_name='ungleichheaderitem',
            name='image',
        ),
        migrations.RemoveField(
            model_name='ungleichheaderwithbackgroundimageslideritem',
            name='background_image',
        ),
        migrations.RemoveField(
            model_name='ungleichheaderwithbackgroundimageslideritem',
            name='cmsplugin_ptr',
        ),
        migrations.RemoveField(
            model_name='ungleichsimpleheader',
            name='background_image',
        ),
        migrations.RemoveField(
            model_name='ungleichsimpleheader',
            name='cmsplugin_ptr',
        ),
        migrations.RemoveField(
            model_name='ungleichsimpleheader',
            name='image',
        ),
        migrations.DeleteModel(
            name='UngleichHeader',
        ),
        migrations.DeleteModel(
            name='UngleichHeaderItem',
        ),
        migrations.DeleteModel(
            name='UngleichHeaderWithBackgroundImageSliderItem',
        ),
        migrations.DeleteModel(
            name='UngleichSimpleHeader',
        ),
    ]