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

    # mula = forms.DateTimeField(widget=DateTimeInput())
    # akhir = forms.DateTimeField(widget=DateTimeInput())
    # TarikhMula = forms.DateTimeField(widget=forms.widgets.DateInput(format="%m/%d/%Y"))

    # # Verify Masa mula mestilah lebih awal daripada masa akhir
    # def clean(self):
    #     data = self.cleaned_data
    #     # print(str(self.cleaned_data['mula'])[:-9],self.cleaned_data['akhir'])
    #     if datetime.strptime(str(self.cleaned_data['mula'])[:-9],'%Y-%m-%d %H:%M') >= datetime.strptime(str(self.cleaned_data['akhir'])[:-9],'%Y-%m-%d %H:%M'):
    #         raise forms.ValidationError("Masa tarikh / masa mula mestilah lebih awal daripada tarikh / masa akhir !")
    #     return data
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

