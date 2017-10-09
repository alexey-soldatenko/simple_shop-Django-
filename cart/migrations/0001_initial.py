# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20170921_1032'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('cart_id', models.CharField(max_length=50)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('quantity', models.PositiveSmallIntegerField()),
                ('product', models.ForeignKey(to='catalog.Product')),
            ],
            options={
                'db_table': 'cart_items',
                'ordering': ['date_add'],
            },
        ),
    ]
