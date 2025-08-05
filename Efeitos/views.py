from django.http import HttpResponseRedirect
from .models import Efeito
from django.shortcuts import render
from .forms import EfeitoForm

def index(request):

    efeitos = Efeito.objects.all()

    return render(request, 'efeito/index.html', {'efeitos': efeitos})

def cria(request):
    if request.method == "POST":
        form = EfeitoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/efeito/")
    else: 
        form = EfeitoForm()


    return render(request, 'efeito/cria.html', {'form': form})

def edita(request, id_efeito):

    efeito = Efeito.objects.get(id=id_efeito)

    if request.method == "POST":
        form = EfeitoForm(request.POST, instance=efeito)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/efeito/")
    else:
        form = EfeitoForm(instance=efeito)
    return render(request, 'efeito/edita.html', {'form': form})

def deleta(request, id_efeito):
    efeito = Efeito.objects.get(id=id_efeito)
    efeito.delete()
    return HttpResponseRedirect("/efeito/")

def detalha(request, id_efeito):

    efeito = Efeito.objects.get(id=id_efeito)

    return render(request, 'efeito/detalhe.html', {'efeito': efeito})