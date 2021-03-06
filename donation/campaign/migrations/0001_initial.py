# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-09 13:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0002_auto_20170806_1821'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('story', models.TextField(null=True)),
                ('amount', models.FloatField(default=0.0)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='category.Category')),
            ],
            options={
                'db_table': 'campaign',
            },
        ),
    ]
