# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=100)),
                ('pub_date', models.DateField(verbose_name='date created')),
            ],
        ),
        migrations.CreateModel(
            name='Smartphone',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('phone_model', models.CharField(max_length=200)),
                ('pub_date', models.DateField(verbose_name='date published')),
                ('producer', models.ForeignKey(to='cellphones.Producer')),
            ],
        ),
    ]
