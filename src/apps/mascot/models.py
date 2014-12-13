# -*- encoding: utf-8 -*-
from django.db import models

from apps.client.models import Client

# Create your models here.
class Species(models.Model):

    name = models.CharField(max_length=20)

    def __unicode__(self):
        return "%s" % (self.name,)


class Race(models.Model):

    name = models.CharField(max_length=20)
    race = models.ForeignKey(Species)

    def __unicode__(self):
        return "%s, %s" % (self.race, self.name)

class Mascot(models.Model):

    # Opciones para el sexo
    SEX_CHOICES = (
        (1, 'Male'), 
        (2, 'Female'),
    )

    name = models.CharField('Nombre', max_length=20)
    owner = models.ForeignKey(Client, related_name='mascot')
    race = models.ForeignKey(Race, related_name='mascot')
    sex = models.PositiveIntegerField('Sexo', max_length=1, choices=SEX_CHOICES)

    def __unicode__(self):
        return "%s, %s" % (self.name, self.owner)