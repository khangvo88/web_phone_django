# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('screen', models.CharField(blank=True, null=True, max_length=100)),
                ('os', models.CharField(blank=True, null=True, max_length=100)),
                ('camera_front', models.CharField(blank=True, null=True, max_length=100)),
                ('cpu', models.CharField(blank=True, null=True, max_length=100)),
                ('ram', models.CharField(blank=True, null=True, max_length=100)),
                ('internal_memory', models.CharField(blank=True, null=True, max_length=100)),
                ('memory_card', models.CharField(blank=True, null=True, max_length=100)),
                ('wireless_tech', models.CharField(blank=True, null=True, max_length=100)),
                ('battery', models.CharField(blank=True, null=True, max_length=100)),
                ('color', models.CharField(blank=True, null=True, max_length=100)),
                ('weight', models.FloatField(blank=True, null=True, default=0)),
                ('com_port', models.CharField(blank=True, null=True, max_length=100)),
                ('connection_type', models.CharField(blank=True, null=True, max_length=100)),
                ('harddisk', models.CharField(blank=True, null=True, max_length=100)),
                ('gpu', models.CharField(blank=True, null=True, max_length=100)),
                ('optical_disk', models.CharField(blank=True, null=True, max_length=100)),
                ('webcam', models.CharField(blank=True, null=True, max_length=100)),
                ('sim_type', models.CharField(blank=True, null=True, max_length=100)),
                ('camera_back', models.CharField(blank=True, null=True, max_length=100)),
                ('design', models.CharField(blank=True, null=True, max_length=100)),
                ('special_features', models.TextField(blank=True, null=True, max_length=100)),
                ('device_type', models.CharField(choices=[(1, 'SMARTPHONE'), (2, 'TABLET'), (3, 'LAPTOP')], max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('model', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('price', models.FloatField(default=0)),
                ('price_1', models.FloatField(verbose_name='New price', default=0)),
                ('pub_date', models.DateField(verbose_name='date published', null=True, blank=True)),
                ('condition', models.CharField(default=1, choices=[(1, 'NEW'), (2, 'LIKE NEW'), (3, 'USED'), (4, 'REFURBRISH')], max_length=20)),
                ('warranty', models.IntegerField(default=12)),
                ('status', models.SmallIntegerField(default=1, choices=[(1, 'STATUS_ACTIVE'), (2, 'STATUS_INACTIVE'), (3, 'STATUS_CLOSED')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['pub_date', 'name'],
            },
        ),
        migrations.CreateModel(
            name='DeviceAccessories',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, default='', max_length=500)),
                ('type', models.CharField(default='Adapter', choices=[('ADAPTER', 'Adapter'), ('HEADPHONE', 'Headphone'), ('MANUAL', 'Manual book'), ('CORD', 'Chargin cord'), ('OTHERS', 'Others')], max_length=10)),
                ('price', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='DeviceAndAccessories',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('is_integrated', models.BooleanField(default=False)),
                ('accessories', models.ForeignKey(to='cellphones.DeviceAccessories')),
                ('device', models.ForeignKey(to='cellphones.Device')),
            ],
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('pub_date', models.DateField(verbose_name='date created', null=True, blank=True)),
                ('email', models.EmailField(blank=True, default='', max_length=254)),
                ('description', models.CharField(blank=True, max_length=1000)),
                ('status', models.SmallIntegerField(default=1, choices=[(1, 'STATUS_ACTIVE'), (2, 'STATUS_INACTIVE'), (3, 'STATUS_CLOSED')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='deviceaccessories',
            name='producer',
            field=models.ForeignKey(to='cellphones.Producer'),
        ),
        migrations.AddField(
            model_name='device',
            name='accessories',
            field=models.ManyToManyField(to='cellphones.DeviceAccessories', through='cellphones.DeviceAndAccessories'),
        ),
        migrations.AddField(
            model_name='device',
            name='producer',
            field=models.ForeignKey(to='cellphones.Producer'),
        ),
    ]
