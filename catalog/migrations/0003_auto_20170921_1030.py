# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20170921_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagonal',
            name='value',
            field=models.DecimalField(unique=True, decimal_places=1, max_digits=3),
        ),
    ]
