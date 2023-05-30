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
    pacientes = Paciente.objects.all().order_by('edad')
    rta = []
    for paciente in pacientes:
        if paciente.idMedico == idMed:
            rta.append(paciente)

    return (rta)