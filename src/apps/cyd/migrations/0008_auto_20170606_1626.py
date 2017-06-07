# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-06-06 16:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cyd', '0007_auto_20170605_1420'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='asignacion',
            options={'verbose_name': 'Asignación', 'verbose_name_plural': 'Asignaciones'},
        ),
        migrations.AlterModelOptions(
            name='crasistencia',
            options={'verbose_name': 'Asistencia de curso', 'verbose_name_plural': 'Asistencias de curso'},
        ),
        migrations.AlterModelOptions(
            name='crhito',
            options={'verbose_name': 'Hito de curso', 'verbose_name_plural': 'Hitos de curso'},
        ),
        migrations.AlterField(
            model_name='asignacion',
            name='grupo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asignados', to='cyd.Grupo'),
        ),
        migrations.AlterField(
            model_name='asignacion',
            name='participante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asignaciones', to='cyd.Participante'),
        ),
        migrations.AlterField(
            model_name='grupo',
            name='sede',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grupos', to='cyd.Sede'),
        ),
    ]
