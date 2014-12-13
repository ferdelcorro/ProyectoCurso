from django.forms import ModelForm, TextInput, DateInput

from apps.client.models import Client


class ClientForm(ModelForm):

    class Meta:
        model = Client
        exclude = ('veterinary',)