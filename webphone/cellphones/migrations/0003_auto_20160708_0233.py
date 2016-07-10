# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cellphones', '0002_smartphone_total_sales'),
    ]

    operations = [
        migrations.AddField(
            model_name='producer',
            name='description',
            field=models.TextField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='producer',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='smartphone',
            name='description',
            field=models.TextField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='smartphone',
            name='price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='smartphone',
            name='phone_model',
            field=models.CharField(max_length=50),
        ),
    ]
