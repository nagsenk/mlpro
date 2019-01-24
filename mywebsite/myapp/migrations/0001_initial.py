# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=128, unique=True)),
                ('password', models.CharField(max_length=128, unique=True)),
                ('email', models.EmailField(max_length=128, unique=True)),
                ('choice', models.CharField(max_length=128, unique=True)),
            ],
        ),
    ]
