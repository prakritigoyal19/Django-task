# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-10-03 15:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('name', models.CharField(max_length=100)),
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]