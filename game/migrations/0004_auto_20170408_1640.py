# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-08 08:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_tag_users'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='platform',
            new_name='platforms',
        ),
    ]
