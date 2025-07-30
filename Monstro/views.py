from django.http import HttpResponseRedirect
from .models import Monstro
from django.shortcuts import render
from .forms import MonstroForm

def index(request):

    monstros = Monstro.objects.all()

    return render(request, 'monstro/index.html', {'monstros': monstros})

def cria(request):
    if request.method == "POST":
        form = MonstroForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/monstro/")
    else: 
        form = MonstroForm()


    return render(request, 'monstro/cria.html', {'form': form})

def edita(request, id_monstro):

    monstro = Monstro.objects.get(id=id_monstro)

    if request.method == "POST":
        form = MonstroForm(request.POST, instance=monstro)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/monstro/")
    else:
        form = MonstroForm(instance=monstro)
    return render(request, 'monstro/edita.html', {'form': form})

def deleta(id_monstro):
    monstro = Monstro.objects.get(id=id_monstro)
    monstro.delete()
    return HttpResponseRedirect("/monstro/")

def detalha(request, id_monstro):

    monstro = Monstro.objects.get(id=id_monstro)

    return render(request, 'monstro/detalhe.html', {'monstro': monstro})