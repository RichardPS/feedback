# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-11-23 13:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_auto_20181113_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='launchquestions',
            name='training',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
            preserve_default=False,
        ),
    ]