# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-07 17:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields
import myapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GenQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poll', models.CharField(max_length=200)),
                ('department', models.CharField(max_length=200)),
                ('votes', jsonfield.fields.JSONField(blank=True, default=dict)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('DP', models.ImageField(blank=True, upload_to='media/DP')),
                ('genPic1', models.ImageField(blank=True, upload_to=myapp.models.user_directory_path)),
                ('genPic2', models.ImageField(blank=True, upload_to=myapp.models.user_directory_path)),
                ('phone', models.CharField(blank=True, max_length=10)),
                ('email', models.CharField(blank=True, max_length=100)),
                ('oneliner', models.CharField(blank=True, max_length=100)),
                ('AnswersAboutMyself', jsonfield.fields.JSONField(blank=True, default=dict)),
                ('VotesIHaveGiven', jsonfield.fields.JSONField(blank=True, default=dict)),
                ('CommentsIWrite', jsonfield.fields.JSONField(blank=True, default=list)),
                ('CommentsIGet', jsonfield.fields.JSONField(blank=True, default=list)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
