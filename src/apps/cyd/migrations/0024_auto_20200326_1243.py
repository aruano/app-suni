# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2020-03-26 18:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cyd', '0023_participante_activo'),
    ]

    operations = [
        migrations.AddField(
            model_name='asignacion',
            name='abandondo',
            field=models.BooleanField(default=False, verbose_name='Abandono'),
        ),
        migrations.AlterField(
            model_name='participante',
            name='dpi',
            field=models.CharField(blank=True, db_index=True, error_messages={'Unico': 'El dpi ya existe'}, max_length=21, null=True, unique=True),
        ),
    ]