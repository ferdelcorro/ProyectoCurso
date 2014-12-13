# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('veterinary', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('telephone', models.CharField(max_length=30)),
                ('veterinary', models.ForeignKey(related_name='client', blank=True, to='veterinary.Veterinary', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
