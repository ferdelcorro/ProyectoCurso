from django.forms import ModelForm, TextInput, DateInput
from apps.mascot.models import Mascot


class MascotForm(ModelForm):

    class Meta:
        model = Mascot
        exclude = ('owner',)