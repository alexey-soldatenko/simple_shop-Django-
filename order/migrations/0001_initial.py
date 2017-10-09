# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20170921_1032'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('cart_id', models.CharField(max_length=50)),
                ('quantity', models.PositiveSmallIntegerField(default=1)),
                ('user_name', models.CharField(max_length=50)),
                ('user_lastname', models.CharField(max_length=70)),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(to='catalog.Product')),
            ],
        ),
    ]
