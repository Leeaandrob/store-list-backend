# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('activity', models.CharField(max_length=255)),
                ('local', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='StoresTxt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Village',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('adress', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('url', models.URLField()),
            ],
        ),
        migrations.AddField(
            model_name='storestxt',
            name='village',
            field=models.OneToOneField(to='stores.Village'),
        ),
        migrations.AddField(
            model_name='store',
            name='village',
            field=models.ForeignKey(to='stores.Village'),
        ),
    ]
