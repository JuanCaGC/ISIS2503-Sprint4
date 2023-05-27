from django.shortcuts import render
from .forms import HistoriaForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .logic.logic_historia import create_historia, get_historias
from pacientes.logic.paciente_logic import get_paciente
import time
from django.contrib.auth.decorators import login_required
from widmy.auth0backend import getRole, getId

@login_required
def historia_list(request):
    role = getRole(request)
    if role == "Medico":
        historias = get_historias()
        context = {
            'historia_list': historias
        }
        return render(request, 'Examen/historias.html', context)
    else:
        return render(request, 'Examen/errorHistoria.html')

@login_required
def historia_create(request):
    role = getRole(request)
    idMedico = getId(request)
    if role == "Medico":

        if request.method == 'POST':
            form = HistoriaForm(request.POST)
            idePaciente = form['paciente'].value()
            pacienteBuscado = get_paciente(idePaciente)
            medicoPaciente = pacienteBuscado.idMedico
            if medicoPaciente != idMedico:
                return render(request, 'Examen/errorHistoria.html')
            if form.is_valid() and medicoPaciente == idMedico:
                create_historia(form)
                messages.add_message(request, messages.SUCCESS, 'Historia creada con exito')
                return HttpResponseRedirect(reverse('historiaCreate'))
            else:
                print(form.errors)
        else:
            form = HistoriaForm()

        context = {
            'form': form,
        }

        return render(request, 'Examen/historiaCreate.html', context)
    else:
        return render(request, 'Examen/errorHistoria.html')