# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-21 17:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0003_users_uni'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='uni',
            new_name='uid',
        ),
    ]