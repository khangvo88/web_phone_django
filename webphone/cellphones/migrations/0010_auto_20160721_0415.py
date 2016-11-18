# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cellphones', '0009_auto_20160720_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='image_ratio',
            field=image_cropping.fields.ImageRatioField('device_image', '400x200', help_text=None, verbose_name='image ratio', hide_image_field=False, free_crop=False, size_warning=False, allow_fullsize=False, adapt_rotation=False),
        ),
    ]
