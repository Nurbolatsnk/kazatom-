# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-22 11:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chink', models.TextField()),
                ('full_name', models.TextField(max_length=255)),
                ('flowmeter_id', models.TextField(max_length=255)),
                ('meter', models.IntegerField()),
                ('counter', models.IntegerField()),
            ],
        ),
    ]
