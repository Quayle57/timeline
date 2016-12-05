# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-02 16:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YupeekTimeline', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='element',
            name='content',
            field=models.CharField(default=None, max_length=2048),
        ),
        migrations.AddField(
            model_name='element',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='element',
            name='start_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='element',
            name='title',
            field=models.CharField(default=None, max_length=255),
        ),
    ]
