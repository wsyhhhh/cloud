# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-05 09:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=32, null=True)),
                ('usbkey', models.CharField(max_length=30)),
                ('kind', models.IntegerField(max_length=2)),
                ('email', models.CharField(max_length=40)),
                ('group_type', models.IntegerField(default=1, max_length=8, null=True)),
                ('admin_type', models.IntegerField(max_length=11)),
                ('reg_time', models.IntegerField(max_length=11, null=True)),
                ('lastlogin', models.IntegerField(max_length=11, null=True)),
                ('log_admin', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='user_log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField(max_length=11, null=True)),
                ('start_time', models.IntegerField(max_length=11, null=True)),
                ('end_time', models.IntegerField(max_length=11, null=True)),
            ],
        ),
    ]
