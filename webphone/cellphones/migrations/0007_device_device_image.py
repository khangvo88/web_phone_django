# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cellphones', '0006_device_on_sale'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='device_image',
            field=models.ImageField(upload_to='device', null=True),
        ),
    ]
