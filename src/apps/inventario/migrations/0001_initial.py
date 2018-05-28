# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-09 13:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crm', '0003_auto_20180509_0727'),
    ]

    operations = [
        migrations.CreateModel(
            name='DescuentoEntrada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'DescuentoEntrada',
                'verbose_name_plural': 'DescuentoEntradas',
            },
        ),
        migrations.CreateModel(
            name='Dispositivo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('triage', models.SlugField(blank=True, editable=False, unique=True)),
                ('serie', models.CharField(blank=True, max_length=80, null=True)),
            ],
            options={
                'verbose_name': 'Dispositivo',
                'verbose_name_plural': 'Dispositivos',
            },
        ),
        migrations.CreateModel(
            name='DispositivoEstado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Estado de dispositivo',
                'verbose_name_plural': 'Estados de dispositivo',
            },
        ),
        migrations.CreateModel(
            name='DispositivoEtapa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proceso', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Etapa de dispositivo',
                'verbose_name_plural': 'Etapas de dispositivo',
            },
        ),
        migrations.CreateModel(
            name='DispositivoMarca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Marca de dispositivo',
                'verbose_name_plural': 'Marcas de dispositivo',
            },
        ),
        migrations.CreateModel(
            name='DispositivoMedida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'Medida',
                'verbose_name_plural': 'Medidas',
            },
        ),
        migrations.CreateModel(
            name='DispositivoModelo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Modelo de dispositivo',
                'verbose_name_plural': 'Modelos de dispositivo',
            },
        ),
        migrations.CreateModel(
            name='DispositivoPuerto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'Puerto',
                'verbose_name_plural': 'Puertos',
            },
        ),
        migrations.CreateModel(
            name='DispositivoRepuesto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_asignacion', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'DispositivoRepuesto',
                'verbose_name_plural': 'DispositivoRepuestos',
            },
        ),
        migrations.CreateModel(
            name='DispositivoTipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=20)),
                ('slug', models.SlugField(unique=True)),
                ('usa_triage', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Tipo de dispositivo',
                'verbose_name_plural': 'Tipos de dispositivo',
            },
        ),
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('en_creacion', models.BooleanField(default=True)),
                ('creada_por', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='entradas_creadas', to=settings.AUTH_USER_MODEL)),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='entradas', to='crm.Donante')),
                ('recibida_por', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='entradas_recibidas', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Entrada',
                'verbose_name_plural': 'Entradas',
            },
        ),
        migrations.CreateModel(
            name='EntradaDetalle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('util', models.PositiveIntegerField(default=0)),
                ('repuesto', models.PositiveIntegerField(default=0)),
                ('desecho', models.PositiveIntegerField(default=0)),
                ('total', models.PositiveIntegerField()),
                ('precio_unitario', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('precio_subtotal', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('precio_descontado', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('precio_total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('creado_por', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('entrada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalles', to='inventario.Entrada')),
                ('tipo_dispositivo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='detalles_entrada', to='inventario.DispositivoTipo')),
            ],
            options={
                'verbose_name': 'Detalle de entrada',
                'verbose_name_plural': 'Detalles de entrada',
            },
        ),
        migrations.CreateModel(
            name='EntradaEstado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
            ],
            options={
                'verbose_name': 'Estado de entrada',
                'verbose_name_plural': 'Estados de entrada',
            },
        ),
        migrations.CreateModel(
            name='EntradaTipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
                ('contable', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Tipo de entrada',
                'verbose_name_plural': 'Tipos de entrada',
            },
        ),
        migrations.CreateModel(
            name='MonitorTipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'Tipo de monitor',
                'verbose_name_plural': 'Tipos de monitor',
            },
        ),
        migrations.CreateModel(
            name='MouseTipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'Tipo de mouse',
                'verbose_name_plural': 'Tipos de mouse',
            },
        ),
        migrations.CreateModel(
            name='Procesador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
            ],
            options={
                'verbose_name': 'Procesador',
                'verbose_name_plural': 'Procesadores',
            },
        ),
        migrations.CreateModel(
            name='PuertoTipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Tipo de puerto',
                'verbose_name_plural': 'Tipos de puerto',
            },
        ),
        migrations.CreateModel(
            name='Repuesto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('disponible', models.BooleanField(default=False)),
                ('entrada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='repuestos', to='inventario.Entrada')),
            ],
            options={
                'verbose_name': 'Repuesto',
                'verbose_name_plural': 'Repuestos',
            },
        ),
        migrations.CreateModel(
            name='RepuestoEstado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
            ],
            options={
                'verbose_name': 'Estado de repuesto',
                'verbose_name_plural': 'Estados de repuesto',
            },
        ),
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Software',
                'verbose_name_plural': 'Software',
            },
        ),
        migrations.CreateModel(
            name='SoftwareTipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=25)),
            ],
            options={
                'verbose_name': 'Tipo de software',
                'verbose_name_plural': 'Tipos de software',
            },
        ),
        migrations.CreateModel(
            name='TipoRed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
            ],
            options={
                'verbose_name': 'Tipo de dispositivo de red',
                'verbose_name_plural': 'Tipos de dispositivos de red',
            },
        ),
        migrations.CreateModel(
            name='VersionSistema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=55)),
                ('so', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='versiones', to='inventario.Software')),
                ('software', models.ManyToManyField(blank=True, to='inventario.Software')),
            ],
            options={
                'verbose_name': 'Versión de sistema',
                'verbose_name_plural': 'Versiones de sistema',
            },
        ),
        migrations.CreateModel(
            name='CPU',
            fields=[
                ('dispositivo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='inventario.Dispositivo')),
                ('indice', models.PositiveIntegerField(editable=False, unique=True)),
                ('ram', models.PositiveIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'dispositivo_cpu',
                'verbose_name': 'CPU',
                'ordering': ['indice'],
                'verbose_name_plural': 'CPUs',
            },
            bases=('inventario.dispositivo',),
        ),
        migrations.CreateModel(
            name='DispositivoRed',
            fields=[
                ('dispositivo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='inventario.Dispositivo')),
                ('indice', models.PositiveIntegerField(editable=False, unique=True)),
                ('cantidad_puertos', models.PositiveIntegerField(blank=True, null=True)),
                ('velocidad', models.PositiveIntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Dispositivo de red',
                'verbose_name_plural': 'Dispositivos de red',
            },
            bases=('inventario.dispositivo',),
        ),
        migrations.CreateModel(
            name='HDD',
            fields=[
                ('dispositivo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='inventario.Dispositivo')),
                ('indice', models.PositiveIntegerField(editable=False, unique=True)),
                ('capacidad', models.PositiveIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'dispositivo_hdd',
                'verbose_name': 'HDD',
                'ordering': ['indice'],
                'verbose_name_plural': 'HDDs',
            },
            bases=('inventario.dispositivo',),
        ),
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('dispositivo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='inventario.Dispositivo')),
                ('indice', models.PositiveIntegerField(editable=False, unique=True)),
                ('ram', models.PositiveIntegerField(blank=True, null=True)),
                ('pulgadas', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
            ],
            options={
                'db_table': 'dispositivo_laptop',
                'verbose_name': 'Laptop',
                'ordering': ['indice'],
                'verbose_name_plural': 'Laptops',
            },
            bases=('inventario.dispositivo',),
        ),
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('dispositivo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='inventario.Dispositivo')),
                ('indice', models.PositiveIntegerField(editable=False, unique=True)),
                ('pulgadas', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
            ],
            options={
                'db_table': 'dispositivo_monitor',
                'verbose_name': 'Monitor',
                'ordering': ['indice'],
                'verbose_name_plural': 'Monitores',
            },
            bases=('inventario.dispositivo',),
        ),
        migrations.CreateModel(
            name='Mouse',
            fields=[
                ('dispositivo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='inventario.Dispositivo')),
                ('indice', models.PositiveIntegerField(editable=False, unique=True)),
            ],
            options={
                'db_table': 'dispositivo_mouse',
                'verbose_name': 'Mouse',
                'ordering': ['indice'],
                'verbose_name_plural': 'Mouses',
            },
            bases=('inventario.dispositivo',),
        ),
        migrations.CreateModel(
            name='Tablet',
            fields=[
                ('dispositivo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='inventario.Dispositivo')),
                ('indice', models.PositiveIntegerField(editable=False, unique=True)),
                ('almacenamiento', models.PositiveIntegerField(blank=True, null=True)),
                ('pulgadas', models.PositiveIntegerField(blank=True, null=True)),
                ('ram', models.PositiveIntegerField(blank=True, null=True)),
                ('almacenamiento_externo', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'dispositivo_tablet',
                'verbose_name': 'Tablet',
                'ordering': ['indice'],
                'verbose_name_plural': 'Tablets',
            },
            bases=('inventario.dispositivo',),
        ),
        migrations.CreateModel(
            name='Teclado',
            fields=[
                ('dispositivo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='inventario.Dispositivo')),
                ('indice', models.PositiveIntegerField(editable=False, unique=True)),
            ],
            options={
                'db_table': 'dispositivo_teclado',
                'verbose_name': 'Teclado',
                'ordering': ['indice'],
                'verbose_name_plural': 'Teclados',
            },
            bases=('inventario.dispositivo',),
        ),
        migrations.AddField(
            model_name='software',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.SoftwareTipo'),
        ),
        migrations.AddField(
            model_name='repuesto',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventario.RepuestoEstado'),
        ),
        migrations.AddField(
            model_name='repuesto',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='repuestos', to='inventario.DispositivoTipo'),
        ),
        migrations.AddField(
            model_name='entrada',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='entradas', to='inventario.EntradaTipo'),
        ),
        migrations.AddIndex(
            model_name='dispositivotipo',
            index=models.Index(fields=['slug'], name='inventario__slug_f8a378_idx'),
        ),
        migrations.AddField(
            model_name='dispositivorepuesto',
            name='asignado_por',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='dispositivorepuesto',
            name='dispositivo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.Dispositivo'),
        ),
        migrations.AddField(
            model_name='dispositivorepuesto',
            name='repuesto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.Repuesto'),
        ),
        migrations.AddField(
            model_name='dispositivopuerto',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventario.PuertoTipo'),
        ),
        migrations.AddField(
            model_name='dispositivoetapa',
            name='estados_disponibles',
            field=models.ManyToManyField(to='inventario.DispositivoEstado'),
        ),
        migrations.AddField(
            model_name='dispositivo',
            name='entrada',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='dispositivos', to='inventario.Entrada'),
        ),
        migrations.AddField(
            model_name='dispositivo',
            name='estado',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventario.DispositivoEstado'),
        ),
        migrations.AddField(
            model_name='dispositivo',
            name='etapa',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to='inventario.DispositivoEtapa'),
        ),
        migrations.AddField(
            model_name='dispositivo',
            name='marca',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventario.DispositivoMarca'),
        ),
        migrations.AddField(
            model_name='dispositivo',
            name='modelo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventario.DispositivoModelo'),
        ),
        migrations.AddField(
            model_name='dispositivo',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.DispositivoTipo'),
        ),
        migrations.AddField(
            model_name='descuentoentrada',
            name='entrada',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='descuentos', to='inventario.Entrada'),
        ),
        migrations.AddField(
            model_name='teclado',
            name='puerto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teclados', to='inventario.DispositivoPuerto'),
        ),
        migrations.AddField(
            model_name='tablet',
            name='medida_almacenamiento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='almacenamiento_tablets', to='inventario.DispositivoMedida'),
        ),
        migrations.AddField(
            model_name='tablet',
            name='medida_ram',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ram_tables', to='inventario.DispositivoMedida'),
        ),
        migrations.AddField(
            model_name='tablet',
            name='procesador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventario.Procesador'),
        ),
        migrations.AddField(
            model_name='tablet',
            name='so_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='so_tablets', to='inventario.Software'),
        ),
        migrations.AddField(
            model_name='tablet',
            name='version_sistema',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='versiones_tablets', to='inventario.VersionSistema'),
        ),
        migrations.AddField(
            model_name='mouse',
            name='puerto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mouses', to='inventario.DispositivoPuerto'),
        ),
        migrations.AddField(
            model_name='mouse',
            name='tipo_mouse',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventario.MouseTipo'),
        ),
        migrations.AddField(
            model_name='monitor',
            name='puerto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='monitores', to='inventario.DispositivoPuerto'),
        ),
        migrations.AddField(
            model_name='monitor',
            name='tipo_monitor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='inventario.MonitorTipo'),
        ),
        migrations.AddField(
            model_name='laptop',
            name='disco_duro',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='laptops', to='inventario.HDD'),
        ),
        migrations.AddField(
            model_name='laptop',
            name='procesador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='inventario.Procesador'),
        ),
        migrations.AddField(
            model_name='laptop',
            name='ram_medida',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventario.DispositivoMedida'),
        ),
        migrations.AddField(
            model_name='laptop',
            name='version_sistema',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='inventario.VersionSistema'),
        ),
        migrations.AddField(
            model_name='hdd',
            name='medida',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventario.DispositivoMedida'),
        ),
        migrations.AddField(
            model_name='hdd',
            name='puerto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hdds', to='inventario.DispositivoPuerto'),
        ),
        migrations.AddField(
            model_name='dispositivored',
            name='puerto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventario.DispositivoPuerto'),
        ),
        migrations.AddField(
            model_name='dispositivored',
            name='velocidad_medida',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventario.DispositivoMedida'),
        ),
        migrations.AddIndex(
            model_name='dispositivo',
            index=models.Index(fields=['triage'], name='inventario__triage_635fd4_idx'),
        ),
        migrations.AddField(
            model_name='cpu',
            name='disco_duro',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='cpus', to='inventario.HDD'),
        ),
        migrations.AddField(
            model_name='cpu',
            name='procesador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='inventario.Procesador'),
        ),
        migrations.AddField(
            model_name='cpu',
            name='ram_medida',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventario.DispositivoMedida'),
        ),
        migrations.AddField(
            model_name='cpu',
            name='version_sistema',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='inventario.VersionSistema'),
        ),
        migrations.AddIndex(
            model_name='teclado',
            index=models.Index(fields=['indice'], name='dispositivo_indice_e381cb_idx'),
        ),
        migrations.AddIndex(
            model_name='tablet',
            index=models.Index(fields=['indice'], name='dispositivo_indice_43d71f_idx'),
        ),
        migrations.AddIndex(
            model_name='mouse',
            index=models.Index(fields=['indice'], name='dispositivo_indice_77febd_idx'),
        ),
        migrations.AddIndex(
            model_name='monitor',
            index=models.Index(fields=['indice'], name='dispositivo_indice_d463b9_idx'),
        ),
        migrations.AddIndex(
            model_name='laptop',
            index=models.Index(fields=['indice'], name='dispositivo_indice_3b14d3_idx'),
        ),
        migrations.AddIndex(
            model_name='hdd',
            index=models.Index(fields=['indice'], name='dispositivo_indice_c83ce6_idx'),
        ),
        migrations.AddIndex(
            model_name='cpu',
            index=models.Index(fields=['indice'], name='dispositivo_indice_c7e156_idx'),
        ),
    ]