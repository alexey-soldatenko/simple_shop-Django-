# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='code',
            field=models.PositiveIntegerField(default=1111),
        ),
        migrations.AlterField(
            model_name='product',
            name='number_in_store',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='was_price',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
