from django.http import HttpResponseRedirect
from .models import item
from django.shortcuts import render
from .forms import ItemForm

def index(request):

    itens = item.objects.all()

    return render(request, 'item/index.html', {'itens': itens})

def cria(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/item/")
    else: 
        form = ItemForm()


    return render(request, 'item/cria.html', {'form': form})

def edita(request, id_item):

    Item = item.objects.get(id=id_item)

    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/item/")
    else:
        form = ItemForm(instance=item)
    return render(request, 'item/edita.html', {'form': form})

def deleta(id_item):
    item = item.objects.get(id=id_item)
    item.delete()
    return HttpResponseRedirect("/item/")

def detalha(request, id_item):

    item = item.objects.get(id=id_item)

    return render(request, 'item/detalhe.html', {'item': item})