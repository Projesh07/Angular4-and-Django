# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-05 07:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0006_auto_20180205_0644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, height_field=b'height_field', max_length=500, null=True, upload_to=b'', width_field=b'width_field'),
        ),
    ]
