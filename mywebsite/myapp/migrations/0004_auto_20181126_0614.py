# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_upload'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='upload',
            new_name='file',
        ),
    ]
