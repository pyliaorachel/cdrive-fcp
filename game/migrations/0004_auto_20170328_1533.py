# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-28 07:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_auto_20170328_1529'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='platform',
            name='id',
        ),
        migrations.AlterField(
            model_name='platform',
            name='platform_name',
            field=models.CharField(choices=[('W', 'Windows'), ('M', 'MacOS'), ('L', 'Linux')], default='W', max_length=2, primary_key=True, serialize=False),
        ),
    ]
