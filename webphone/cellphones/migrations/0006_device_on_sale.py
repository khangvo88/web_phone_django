# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cellphones', '0005_device_is_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='on_sale',
            field=models.BooleanField(default=False, verbose_name='On Sale'),
        ),
    ]
