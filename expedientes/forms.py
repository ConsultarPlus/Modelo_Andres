from django import forms

from .models import Expedientes
from functools import partial
DateInput = partial(forms.DateInput, {'class': 'datepicker'})


class ExpedienteForm(forms.ModelForm):
    choice = ['2']
    observacion = forms.CharField(widget=forms.Textarea())
    fecha_inicio = forms.DateField(widget=DateInput())

    class Meta:
        model = Expedientes
        fields = [
            'id',
            'tipo_reclamo',
            # 'user_carga',
            'fecha_inicio',
            'observacion'
        ]

#    def clean_observacion(self):
