from django.http import HttpResponseRedirect
from .models import Dungeon
from django.shortcuts import render
from .forms import DungeonForm

def index(request):

    dungeons = Dungeon.objects.all()

    return render(request, 'dungeon/index.html', {'dungeons': dungeons})

def cria(request):
    if request.method == "POST":
        form = DungeonForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/dungeon/")
    else: 
        form = DungeonForm()


    return render(request, 'dungeon/cria.html', {'form': form})

def edita(request, id_dungeon):

    dungeon = Dungeon.objects.get(id=id_dungeon)

    if request.method == "POST":
        form = DungeonForm(request.POST, instance=dungeon)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/dungeon/")
    else:
        form = DungeonForm(instance=dungeon)
    return render(request, 'dungeon/edita.html', {'form': form})

def deleta(id_dungeon):
    dungeon = Dungeon.objects.get(id=id_dungeon)
    dungeon.delete()
    return HttpResponseRedirect("/dungeon/")

def detalha(request, id_dungeon):

    dungeon = Dungeon.objects.get(id=id_dungeon)

    return render(request, 'dungeon/detalhe.html', {'dungeon': dungeon})