from django import forms
from django.forms import formset_factory
# from multi_email_field.forms import MultiEmailField
from .models import Auditee, SubAuditee
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from datetime import datetime
from Pentadbir.models import Sistem



STATUS_CHOICES = [
	(0, 'Tidak Aktif'),
	(1, 'Aktif'),
]


class AuditeeForm(forms.ModelForm):
    Status = forms.ChoiceField(choices=STATUS_CHOICES, required=True)

    class Meta:
        model = Auditee
        fields = ('NamaAuditee', 'Status', 'SistemID')


class SubAuditeeForm(forms.ModelForm):

    Status = forms.ChoiceField(choices=STATUS_CHOICES, required=True)

    class Meta:
        model = SubAuditee
        fields = ('NamaSubAuditee', 'AuditeeID', 'Status')


class SubauditeeForm2(forms.Form):
    NamaSubAuditee = forms.CharField(
        label='Sub Auditee',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Sila isi sub auditee'
        })
    )


SubauditeeFormset2 = formset_factory(SubauditeeForm2)
# SubauditeeFormset = formset_factory(SubauditeeForm2, extra=1)


