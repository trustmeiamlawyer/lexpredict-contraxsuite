# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-17 18:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lease', '0014_auto_20171213_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leasedocument',
            name='rent_due_frequency',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
