# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cellphones', '0010_auto_20160721_0415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='image_ratio',
            field=image_cropping.fields.ImageRatioField('device_image', '241x212', adapt_rotation=False, hide_image_field=False, free_crop=False, verbose_name='image ratio', help_text=None, allow_fullsize=False, size_warning=False),
        ),
    ]
