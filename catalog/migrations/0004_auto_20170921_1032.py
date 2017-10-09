# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20170921_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weight',
            name='value',
            field=models.DecimalField(max_digits=3, decimal_places=1, unique=True),
        ),
    ]
