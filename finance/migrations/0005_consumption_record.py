# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-21 17:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0004_auto_20170121_1735'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consumption_record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField(max_length=30)),
                ('amount', models.CharField(max_length=30)),
                ('group_id', models.IntegerField(default=0, max_length=30)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.Users')),
            ],
        ),
    ]
