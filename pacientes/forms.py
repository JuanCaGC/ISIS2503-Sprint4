
from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = [
            'name',
            'identificacion',
            'idMedico'
        ]
        labels = {
            'name': 'Name',
            'identificacion': 'Identificacion',
            'idMedico': 'Identificacion Medico'
        }