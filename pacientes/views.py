
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import PacienteForm
from .logic.paciente_logic import get_pacientes, create_paciente, get_pacientesPorMedico
from django.contrib.auth.decorators import login_required
from widmy.auth0backend import getRole, getId


@login_required
def paciente_list(request):
    role = getRole(request)
    if role == "Medico" or role=="Enfermera":
        pacientes = get_pacientes()
        context = {
            'paciente_list': pacientes
        }
        return render(request, 'Pacientes/pacientes.html', context)
    else:
        return render(request, 'Pacientes/errorPaciente.html')

@login_required
def pacientes_medico(request):
    role = getRole(request)
    print(role)
    if role == "Medico":
        print(role)
        return render(request, 'Pacientes/errorPaciente.html')
    else:
        return render(request, 'Pacientes/errorPaciente.html')


@login_required
def paciente_create(request):
    role = getRole(request)
    if role == "Medico":
        if request.method == 'POST':
            form = PacienteForm(request.POST)
            if form.is_valid():
                create_paciente(form)
                messages.add_message(request, messages.SUCCESS, 'Un Paciente ha sido creado exitosamente')
                return HttpResponseRedirect(reverse('pacienteCreate'))
            else:
                print(form.errors)
        else:
            form = PacienteForm()

        context = {
            'form': form,
        }
        return render(request, 'Pacientes/pacienteCreate.html', context)
    else:
        return render(request, 'Pacientes/errorPaciente.html')
