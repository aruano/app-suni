# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-01-24 20:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0040_auto_20190110_1038'),
    ]

    operations = [
        migrations.AddField(
            model_name='cpu',
            name='all_in_one',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='repuesto',
            name='marca',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventario.DispositivoMarca'),
        ),
        migrations.AddField(
            model_name='repuesto',
            name='modelo',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
