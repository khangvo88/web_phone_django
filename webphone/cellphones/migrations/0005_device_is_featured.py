# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cellphones', '0004_auto_20160717_2338'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='is_featured',
            field=models.BooleanField(default=False, verbose_name='Featured Product'),
        ),
    ]
