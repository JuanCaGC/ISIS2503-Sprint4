from ..models import Paciente

def get_pacientes():
    queryset = Paciente.objects.all()
    return (queryset)

def create_paciente(form):
    examen = form.save()
    examen.save()
    return ()

def get_paciente(pkd):
    paciente = Paciente.objects.get(pk=pkd)
    return (paciente)


def get_pacientesPorMedico(idMed):
    print(idMed)
    pacientes = Paciente.objects.get(Paciente.idMedico==idMed)
    return (pacientes)