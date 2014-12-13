# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('veterinary', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Veterinarian',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('telephone', models.CharField(max_length=30)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('veterinary', models.ForeignKey(related_name='veterinarian', blank=True, to='veterinary.Veterinary', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
