# -*- coding: utf-8 *-*
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

from apps.veterinarian.models import Veterinarian


class VeterinarianForm(ModelForm):

    class Meta:
        model = Veterinarian

        exclude = {
            'veterinary'
        }
