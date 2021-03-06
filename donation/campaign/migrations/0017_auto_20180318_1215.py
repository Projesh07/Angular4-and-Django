# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-18 12:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0016_campaign_is_highlighted'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialShare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_network', models.CharField(choices=[(b'facebook', b'FACEBOOK'), (b'google', b'GOOGLE'), (b'linkdin', b'LINKDIN'), (b'twitter', b'TWITTER')], max_length=255)),
                ('count', models.IntegerField(default=1, max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'campaign_socialnetwork_shares',
            },
        ),
        migrations.AlterField(
            model_name='campaign',
            name='is_highlighted',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='socialshare',
            name='campaign',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='campaign_share', to='campaign.Campaign'),
        ),
    ]
