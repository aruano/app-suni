# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2020-01-13 16:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cyd', '0020_sede_activa'),
    ]

    operations = [
        migrations.AddField(
            model_name='grupo',
            name='activo',
            field=models.BooleanField(default=True, verbose_name='Activo'),
        ),
    ]
