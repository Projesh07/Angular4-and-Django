# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-12 19:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0013_auto_20170821_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
