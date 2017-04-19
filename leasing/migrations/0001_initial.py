# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-19 08:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import enumfields.fields
import leasing.enums


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', enumfields.fields.EnumField(enum=leasing.enums.ApplicationType, max_length=255, verbose_name='Application type')),
                ('is_open', models.BooleanField(default=False, verbose_name='Is an open application')),
                ('reasons', models.TextField(blank=True, null=True, verbose_name='Application reasons')),
                ('lease_start_date', models.DateField(blank=True, null=True, verbose_name='Lease start date')),
                ('lease_end_date', models.DateField(blank=True, null=True, verbose_name='Lease end date')),
                ('lease_is_reservation', models.BooleanField(default=False, verbose_name='Lease is a reservation')),
                ('lease_is_short_term', models.BooleanField(default=False, verbose_name='Lease is short term')),
                ('lease_is_long_term', models.BooleanField(default=False, verbose_name='Lease is long term')),
                ('lease_short_term_reason', enumfields.fields.EnumField(blank=True, enum=leasing.enums.ShortTermReason, max_length=255, null=True, verbose_name='Reason for short term lease')),
                ('organization_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Organization name')),
                ('organization_address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Organization address')),
                ('organization_is_company', models.BooleanField(default=False, verbose_name='Is organization a company')),
                ('organization_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='Organization id')),
                ('organization_revenue', models.CharField(blank=True, max_length=255, null=True, verbose_name='Organization revenue')),
                ('contact_person', models.CharField(blank=True, max_length=255, null=True, verbose_name='Contact person')),
                ('contact_address', models.CharField(blank=True, max_length=2048, null=True, verbose_name='Contacts address')),
                ('contact_billing_address', models.CharField(blank=True, max_length=2048, null=True, verbose_name='Contacts billing address')),
                ('contact_electronic_billing', models.CharField(blank=True, max_length=2048, null=True, verbose_name='Contacts electronic billing details')),
                ('contact_email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Contacts email address')),
                ('contact_phone', models.CharField(blank=True, max_length=255, null=True, verbose_name='Contacts phone number')),
                ('land_area', models.IntegerField(blank=True, null=True, verbose_name='Land area in full square meters')),
                ('land_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='Land id')),
                ('land_address', models.CharField(blank=True, max_length=2048, null=True, verbose_name='Land address')),
                ('land_map_link', models.CharField(blank=True, max_length=2048, null=True, verbose_name='Land map link')),
            ],
        ),
        migrations.CreateModel(
            name='BuildingFootprint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('use', models.CharField(blank=True, max_length=2048, null=True, verbose_name='Use')),
                ('area', models.IntegerField(blank=True, null=True, verbose_name='Area in full square meters')),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='building_footprints', to='leasing.Application')),
            ],
        ),
    ]
