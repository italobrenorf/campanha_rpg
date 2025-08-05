from django.http import HttpResponseRedirect
from .models import Evento
from django.shortcuts import render
from .forms import EventoForm

def index(request):

    eventos = Evento.objects.all()

    return render(request, 'evento/index.html', {'eventos': eventos})

def cria(request):
    if request.method == "POST":
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/evento/")
    else: 
        form = EventoForm()


    return render(request, 'evento/cria.html', {'form': form})

def edita(request, id_evento):

    evento = Evento.objects.get(id=id_evento)

    if request.method == "POST":
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/evento/")
    else:
        form = EventoForm(instance=evento)
    return render(request, 'evento/edita.html', {'form': form})

def deleta(request, id_evento):
    evento = Evento.objects.get(id=id_evento)
    evento.delete()
    return HttpResponseRedirect("/evento/")

def detalha(request, id_evento):

    evento = Evento.objects.get(id=id_evento)

    return render(request, 'evento/detalhe.html', {'evento': evento})