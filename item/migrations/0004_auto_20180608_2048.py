# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-06-08 12:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_africa_america_china_europe_middleasia_oceania_southeastasia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Itinerary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('month', models.CharField(max_length=2)),
                ('day', models.CharField(max_length=2)),
                ('price', models.CharField(max_length=6)),
                ('region', models.CharField(max_length=13)),
                ('agency', models.CharField(max_length=10)),
                ('status', models.CharField(max_length=10)),
                ('link', models.URLField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Africa',
        ),
        migrations.DeleteModel(
            name='America',
        ),
        migrations.DeleteModel(
            name='China',
        ),
        migrations.DeleteModel(
            name='Europe',
        ),
        migrations.DeleteModel(
            name='MiddleAsia',
        ),
        migrations.DeleteModel(
            name='NorthEastAsia',
        ),
        migrations.DeleteModel(
            name='Oceania',
        ),
        migrations.DeleteModel(
            name='SouthEastAsia',
        ),
    ]