from django.forms import ModelForm, Textarea


from apps.clinic_history.models import ClinicHistory

class HistoryForm(ModelForm):

    class Meta:
        model = ClinicHistory
        exclude = ('mascot',)
        include = ('date_analysis',)

        widgets = {
            'date_analysis': Textarea(attrs={'cols': 50 , 'rows': 5}),
        }