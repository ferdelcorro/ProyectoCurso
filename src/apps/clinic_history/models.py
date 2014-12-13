# -*- encoding: utf-8 -*-
from django.db import models

from datetime import datetime

from apps.mascot.models import Mascot

# Create your models here.
class ClinicHistory(models.Model):

    mascot = models.ForeignKey(Mascot, related_name='mascot')
    date_analysis = models.DateTimeField('Fecha', auto_now_add=True)
    notas = models.CharField('Notas', max_length=250)

    def __unicode__(self):
        return "%s, %s" % (self.mascot, self.date_analysis)