# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cellphones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='smartphone',
            name='total_sales',
            field=models.IntegerField(default=0),
        ),
    ]
