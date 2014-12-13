from django.forms import ModelForm, TextInput, DateInput
from apps.veterinary.models import Veterinary


class VeterinaryForm(ModelForm):

    class Meta:
        model = Veterinary
        exclude = ('location',)