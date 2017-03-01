# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-03-13 07:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities_light', '0007_make_country_name_not_unique'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='timezone',
            field=models.CharField(blank=True, db_index=True, max_length=40, null=True),
        ),
    ]
