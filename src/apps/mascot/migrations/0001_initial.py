# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mascot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('sex', models.PositiveIntegerField(max_length=1, choices=[(b'1', b'Male'), (b'2', b'Female')])),
                ('photo', easy_thumbnails.fields.ThumbnailerImageField(upload_to=b'mascots')),
                ('birthday', models.DateField(null=True, blank=True)),
                ('owner', models.ForeignKey(related_name='mascot', to='client.Client')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='race',
            name='race',
            field=models.ForeignKey(to='mascot.Species'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mascot',
            name='race',
            field=models.ForeignKey(related_name='mascot', to='mascot.Race'),
            preserve_default=True,
        ),
    ]
