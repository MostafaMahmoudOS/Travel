# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-21 14:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experience', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='rate',
            field=models.IntegerField(default=1),
        ),
    ]