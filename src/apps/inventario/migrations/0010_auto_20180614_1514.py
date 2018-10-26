# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-06-14 21:14
from __future__ import unicode_literals

from django.db import migrations


from django.core.management import call_command

fixtures = ['dispositivo_estado', 'dispositivo_etapa']


def load_fixture(apps, schema_editor):
    for fixture in fixtures:
        call_command('loaddata', fixture, app_label='inventario')


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0009_auto_20180614_1007'),
    ]

    operations = [
        migrations.RunPython(load_fixture)
    ]