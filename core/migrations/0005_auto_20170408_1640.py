# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-08 08:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20170408_1310'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='game',
            new_name='games',
        ),
    ]