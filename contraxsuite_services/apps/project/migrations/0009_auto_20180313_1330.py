# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-13 13:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0008_uploadsession_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadsession',
            name='completed',
            field=models.BooleanField(db_index=True, default=False),
        ),
    ]
