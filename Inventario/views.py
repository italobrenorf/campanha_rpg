from django.http import HttpResponseRedirect
from .models import Inventario
from django.shortcuts import render
from .forms import InventarioForm

def index(request):

    inventarios = Inventario.objects.all()

    return render(request, 'inventario/index.html', {'inventarios': inventarios})

def cria(request):
    if request.method == "POST":
        form = InventarioForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/inventario/")
    else: 
        form = InventarioForm()


    return render(request, 'inventario/cria.html', {'form': form})

def edita(request, id_inventario):

    inventario = Inventario.objects.get(id=id_inventario)

    if request.method == "POST":
        form = InventarioForm(request.POST, instance=inventario)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/inventario/")
    else:
        form = InventarioForm(instance=inventario)
    return render(request, 'inventario/edita.html', {'form': form})

def deleta(request, id_inventario):
    inventario = Inventario.objects.get(id=id_inventario)
    inventario.delete()
    return HttpResponseRedirect("/inventario/")

def detalha(request, id_inventario):

    inventario = Inventario.objects.get(id=id_inventario)

    return render(request, 'inventario/detalhe.html', {'inventario': inventario})