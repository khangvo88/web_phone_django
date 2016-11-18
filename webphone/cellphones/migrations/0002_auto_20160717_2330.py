# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cellphones', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='device',
            old_name='device_type',
            new_name='category',
        ),
        migrations.AlterField(
            model_name='device',
            name='status',
            field=models.SmallIntegerField(choices=[(1, 'ACTIVE'), (2, 'INACTIVE'), (3, 'CLOSED')], default=1),
        ),
        migrations.AlterField(
            model_name='producer',
            name='status',
            field=models.SmallIntegerField(choices=[(1, 'ACTIVE'), (2, 'INACTIVE'), (3, 'CLOSED')], default=1),
        ),
    ]
