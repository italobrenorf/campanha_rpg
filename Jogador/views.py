from django.http import HttpResponseRedirect
from .models import Jogador
from django.shortcuts import render
from .forms import JogadorForm

def index(request):

    jogadores = Jogador.objects.all()

    return render(request, 'jogador/index.html', {'jogadores': jogadores})

def cria(request):
    if request.method == "POST":
        form = JogadorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/jogador/")
    else: 
        form = JogadorForm()


    return render(request, 'jogador/cria.html', {'form': form})

def edita(request, id_jogador):

    jogador = Jogador.objects.get(id=id_jogador)

    if request.method == "POST":
        form = JogadorForm(request.POST, instance=jogador)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/jogador/")
    else:
        form = JogadorForm(instance=jogador)
    return render(request, 'jogador/edita.html', {'form': form})

def deleta(id_jogador):
    jogador = Jogador.objects.get(id=id_jogador)
    jogador.delete()
    return HttpResponseRedirect("/jogador/")

def detalha(request, id_jogador):

    jogador = Jogador.objects.get(id=id_jogador)

    return render(request, 'jogador/detalhe.html', {'jogador': jogador})