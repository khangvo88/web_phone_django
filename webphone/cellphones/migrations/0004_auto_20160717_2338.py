# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cellphones', '0003_auto_20160717_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='category',
            field=models.SmallIntegerField(choices=[(1, 'SMARTPHONE'), (2, 'TABLET'), (3, 'LAPTOP')], default=1),
        ),
        migrations.AlterField(
            model_name='producer',
            name='pub_date',
            field=models.DateField(default=datetime.date(2010, 1, 1), verbose_name='published on', null=True, blank=True),
        ),
    ]
