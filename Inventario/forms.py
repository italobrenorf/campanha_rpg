from .models import Inventario
from django.forms import ModelForm

class InventarioForm(ModelForm):
    class Meta: 
        model =  Inventario
        fields = ['personagem','item', 'quantidade', 'equipado']