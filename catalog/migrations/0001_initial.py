# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('meta_keywords', models.CharField(help_text='Comma-delimited set of SEO keywords for meta tag', max_length=255, verbose_name='Meta Keywords')),
                ('meta_description', models.CharField(help_text='Content for description meta tag', max_length=255, verbose_name='Meta description')),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Diagonal',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('value', models.DecimalField(decimal_places=1, max_digits=2, unique=True)),
            ],
            options={
                'db_table': 'diagonal',
            },
        ),
        migrations.CreateModel(
            name='Display',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('value', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'db_table': 'display',
            },
        ),
        migrations.CreateModel(
            name='DVD',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('value', models.CharField(max_length=10, unique=True)),
            ],
            options={
                'db_table': 'dvd',
            },
        ),
        migrations.CreateModel(
            name='Grafic',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('value', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'db_table': 'grafic',
            },
        ),
        migrations.CreateModel(
            name='HDD',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('value', models.IntegerField(unique=True)),
            ],
            options={
                'db_table': 'hdd',
            },
        ),
        migrations.CreateModel(
            name='Kind',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('value', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'db_table': 'kind',
            },
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('value', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'db_table': 'manufacturer',
            },
        ),
        migrations.CreateModel(
            name='OS',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('value', models.CharField(max_length=15, unique=True)),
            ],
            options={
                'db_table': 'os',
            },
        ),
        migrations.CreateModel(
            name='Processor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('value', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'db_table': 'processor',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('description', models.TextField()),
                ('meta_keywords', models.CharField(help_text='Comma-delimited set of SEO keywords for meta tag', max_length=255)),
                ('meta_description', models.CharField(help_text='Content for description meta tag', max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('number_in_store', models.IntegerField()),
                ('was_price', models.IntegerField(default=0)),
                ('has_price', models.IntegerField()),
                ('create_date', models.DateField(auto_now_add=True)),
                ('update_date', models.DateField(auto_now=True)),
                ('category', models.ForeignKey(to='catalog.Category')),
                ('diagonal', models.ForeignKey(to='catalog.Diagonal')),
                ('display', models.ForeignKey(to='catalog.Display')),
                ('dvd', models.ForeignKey(to='catalog.DVD')),
                ('grafic', models.ForeignKey(to='catalog.Grafic')),
                ('hdd', models.ForeignKey(to='catalog.HDD')),
                ('kind', models.ForeignKey(to='catalog.Kind')),
                ('manufacturer', models.ForeignKey(to='catalog.Manufacturer')),
                ('os', models.ForeignKey(to='catalog.OS')),
                ('processor', models.ForeignKey(to='catalog.Processor')),
            ],
            options={
                'ordering': ['name', 'is_active'],
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='RAM',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('value', models.IntegerField(unique=True)),
            ],
            options={
                'db_table': 'ram',
            },
        ),
        migrations.CreateModel(
            name='WebCam',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('value', models.CharField(max_length=15, unique=True)),
            ],
            options={
                'db_table': 'webcam',
            },
        ),
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('value', models.DecimalField(decimal_places=1, max_digits=2, unique=True)),
            ],
            options={
                'db_table': 'weight',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='ram',
            field=models.ForeignKey(to='catalog.RAM'),
        ),
        migrations.AddField(
            model_name='product',
            name='webcam',
            field=models.ForeignKey(to='catalog.WebCam'),
        ),
        migrations.AddField(
            model_name='product',
            name='weight',
            field=models.ForeignKey(to='catalog.Weight'),
        ),
    ]
