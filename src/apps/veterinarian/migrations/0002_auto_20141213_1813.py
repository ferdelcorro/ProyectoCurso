# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('veterinarian', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veterinarian',
            name='telephone',
            field=models.CharField(max_length=30, verbose_name=b'Tel\xc3\xa9fono'),
            preserve_default=True,
        ),
    ]
