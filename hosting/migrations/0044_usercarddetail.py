# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-10-15 19:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import utils.mixins


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0006_auto_20160526_0445'),
        ('hosting', '0043_vmdetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCardDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last4', models.CharField(max_length=4)),
                ('brand', models.CharField(max_length=10)),
                ('fingerprint', models.CharField(max_length=100)),
                ('exp_month', models.IntegerField()),
                ('exp_year', models.IntegerField()),
                ('preferred', models.BooleanField(default=False)),
                ('stripe_customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='membership.StripeCustomer')),
            ],
            options={
                'permissions': (('view_usercarddetail', 'View User Card'),),
            },
            bases=(utils.mixins.AssignPermissionsMixin, models.Model),
        ),
    ]
