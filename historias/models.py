from django.db import models
from pacientes.models import Paciente

class Historia(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, default=None)
    descripcion = models.CharField(max_length=2000)
    dateTime = models.DateTimeField(auto_now_add=True)
    examenes = models.CharField(max_length=2000)
    medicamentos = models.CharField(max_length=1000)

    def __str__(self):
        return '%s %s' % (self.paciente, self.descripcion)