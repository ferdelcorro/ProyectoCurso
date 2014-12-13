# -*- encoding: utf-8 -*-
from django.db import models

from apps.veterinary.models import Veterinary

# Create your models here.

class Client(models.Model):
    
    name = telephone = models.CharField(max_length=30)
    telephone = models.CharField(max_length=30)
    veterinary = models.ForeignKey(Veterinary, null=True, blank=True,
                    related_name='client'
                )

    def __unicode__(self):
        return "%s, %s" % (self.name, self.veterinary)