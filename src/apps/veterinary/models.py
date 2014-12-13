# -*- encoding: utf-8 -*-
from django.db import models

from apps.core.models import Citie

# Create your models here.
class Veterinary(models.Model):
    
    name = models.CharField('Veterinary name', max_length=30)
    location = models.ForeignKey(Citie, null=True, blank=True)
    direction = models.CharField('Dirección', max_length=30)

    def __unicode__(self):
        return "%s" % (self.name,)