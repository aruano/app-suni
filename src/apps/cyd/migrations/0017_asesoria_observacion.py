# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-07-31 14:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cyd', '0016_auto_20170728_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='asesoria',
            name='observacion',
            field=models.TextField(blank=True, null=True, verbose_name='Observaciones'),
        ),
    ]