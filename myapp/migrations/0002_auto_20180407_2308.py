# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-07 17:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='DP',
            field=models.ImageField(blank=True, upload_to='DP'),
        ),
    ]
