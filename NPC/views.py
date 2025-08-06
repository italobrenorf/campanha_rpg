from django.http import HttpResponseRedirect
from .models import Npc
from django.shortcuts import render
from .forms import NpcForm

def index(request):

    npcs = Npc.objects.all()

    return render(request, 'npc/index.html', {'npcs': npcs})

def cria(request):
    if request.method == "POST":
        form = NpcForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/npc/")
    else: 
        form = NpcForm()


    return render(request, 'npc/cria.html', {'form': form})

def edita(request, id_npc):

    npc = Npc.objects.get(id=id_npc)

    if request.method == "POST":
        form = NpcForm(request.POST, instance=npc)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/npc/")
    else:
        form = NpcForm(instance=npc)
    return render(request, 'npc/edita.html', {'form': form})

def deleta(id_npc):
    npc = Npc.objects.get(id=id_npc)
    npc.delete()
    return HttpResponseRedirect("/npc/")

def detalha(request, id_npc):

    npc = Npc.objects.get(id=id_npc)

    return render(request, 'npc/detalhe.html', {'npc': npc})