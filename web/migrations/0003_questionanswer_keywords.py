# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-07-03 05:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20180703_1024'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionanswer',
            name='keywords',
            field=models.CharField(max_length=150, null=True),
        ),
    ]