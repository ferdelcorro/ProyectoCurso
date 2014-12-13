# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('veterinary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veterinary',
            name='direction',
            field=models.CharField(max_length=30, verbose_name=b'Direcci\xc3\xb3n'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='veterinary',
            name='name',
            field=models.CharField(max_length=30, verbose_name=b'Veterinary name'),
            preserve_default=True,
        ),
    ]
