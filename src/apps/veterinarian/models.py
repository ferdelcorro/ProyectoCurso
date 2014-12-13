# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

from apps.veterinary.models import Veterinary


class Veterinarian(models.Model):
    
    user = models.ForeignKey(User)
    veterinary = models.ForeignKey(Veterinary, null=True, blank=True,
                    related_name='veterinarian'
                )
    telephone = models.CharField('Teléfono', max_length=30)

    def __unicode__(self):
        return "%s" % (self.user.username,)