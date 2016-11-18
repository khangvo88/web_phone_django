# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cellphones', '0007_device_device_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='image_ratio',
            field=image_cropping.fields.ImageRatioField('device_image', '400x300', allow_fullsize=False, free_crop=False, adapt_rotation=False, size_warning=False, hide_image_field=False, verbose_name='image ratio', help_text=None),
        ),
        migrations.AlterField(
            model_name='device',
            name='device_image',
            field=models.ImageField(upload_to='raw', null=True),
        ),
    ]
