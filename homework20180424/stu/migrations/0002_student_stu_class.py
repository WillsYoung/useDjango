# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-24 13:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='stu_class',
            field=models.CharField(default=0, max_length=12),
        ),
    ]
