# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cellphones', '0008_auto_20160720_0929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='image_ratio',
            field=image_cropping.fields.ImageRatioField('device_image', '241x212', help_text=None, adapt_rotation=False, free_crop=False, hide_image_field=False, verbose_name='image ratio', size_warning=False, allow_fullsize=False),
        ),
    ]
