from django import forms
from .models import Sesi
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from datetime import datetime

STATUS_CHOICES = [
    (0, 'TIDAK AKTIF'),
    (1, 'AKTIF'),
]
class DateInput(forms.DateInput):
    input_type = 'date'
    input_formats = ['%d/%m/%Y']

class SesiForm(forms.ModelForm):

    Status = forms.ChoiceField(choices=STATUS_CHOICES, required=True)
    class Meta:
        model = Sesi
        fields = ('Siri', 'TarikhMula', 'TarikhTamat', 'TarikhMulaAudit','TarikhTamatAudit', 'Status',)
        # fields ="__all__"
        # fields = ('Siri', 'Status', 'SistemID',)
        widgets = {
            'TarikhMula': DateInput(),
            'TarikhTamat': DateInput(),
            'TarikhMulaAudit': DateInput(),
            'TarikhTamatAudit': DateInput(),

        }
    #Status= forms.Select(widget=forms.Select(choices=STATUS_CHOICES))

