# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-07-06 08:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrar', '0003_auto_20180706_0812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='computadora',
            field=models.CharField(max_length=4),
        ),
    ]
