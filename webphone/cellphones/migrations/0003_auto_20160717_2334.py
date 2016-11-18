# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cellphones', '0002_auto_20160717_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='category',
            field=models.SmallIntegerField(choices=[(1, 'SMARTPHONE'), (2, 'TABLET'), (3, 'LAPTOP')]),
        ),
        migrations.AlterField(
            model_name='device',
            name='condition',
            field=models.SmallIntegerField(default=1, choices=[(1, 'NEW'), (2, 'LIKE NEW'), (3, 'USED'), (4, 'REFURBRISH')]),
        ),
    ]
