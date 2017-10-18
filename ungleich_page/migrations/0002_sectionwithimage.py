# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-10-18 22:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0004_auto_20160328_1434'),
        ('ungleich_page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SectionWithImage',
            fields=[
                ('ungelichpicture_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ungleich_page.UngelichPicture')),
                ('price_tag_url', models.URLField(default='', max_length=300)),
                ('price_tag_image', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='price_tag_image', to='filer.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('ungleich_page.ungelichpicture',),
        ),
    ]
