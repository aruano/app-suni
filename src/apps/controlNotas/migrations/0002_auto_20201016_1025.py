# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2020-10-16 16:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('controlNotas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluacion',
            name='materia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='materias', to='controlNotas.Materia'),
        ),
        migrations.AlterField(
            model_name='evaluacion',
            name='visita',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visitas', to='controlNotas.Visita'),
        ),
    ]