# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mascot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascot',
            name='birthday',
            field=models.DateField(null=True, verbose_name=b'Fecha de nacimiento', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mascot',
            name='name',
            field=models.CharField(max_length=20, verbose_name=b'Nombre'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mascot',
            name='photo',
            field=easy_thumbnails.fields.ThumbnailerImageField(upload_to=b'mascots', null=True, verbose_name=b'Foto', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mascot',
            name='sex',
            field=models.PositiveIntegerField(max_length=1, verbose_name=b'Sexo', choices=[(1, b'Male'), (2, b'Female')]),
            preserve_default=True,
        ),
    ]
