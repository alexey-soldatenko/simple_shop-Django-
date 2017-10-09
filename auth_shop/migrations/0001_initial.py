# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.auth.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, to=settings.AUTH_USER_MODEL, parent_link=True, serialize=False, primary_key=True)),
                ('phone', models.CharField(max_length=20)),
                ('cart_id', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'my_users',
                'ordering': ['first_name'],
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
