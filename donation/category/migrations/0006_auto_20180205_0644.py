# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-05 06:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0005_auto_20180204_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, height_field=b'height_field', null=True, upload_to=b'', width_field=b'width_field'),
        ),
    ]
