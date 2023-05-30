
from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = [
            'name',
            'identificacion',
            'edad',
            'idMedico'
        ]
        labels = {
            'name': 'Name',
            'identificacion': 'Identificacion',
            'edad': 'Edad',
            'idMedico': 'Identificacion Medico'
        }