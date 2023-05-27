from django import forms
from .models import Historia

class HistoriaForm(forms.ModelForm):
    class Meta:
        model = Historia
        fields = [
            'paciente',
            'descripcion',
            'examenes',
            'medicamentos',
            #'dateTime',
        ]

        labels = {
            'paciente' : 'Paciente',
            'descripcion' : 'Descripcion',
            'examanes' : 'Examen',
            'medicamentos' : 'Medicamento'
            #'dateTime' : 'Date Time',
        }