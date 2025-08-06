from .models import Npc
from django.forms import ModelForm

class NpcForm(ModelForm):
    class Meta: 
        model =  Npc
        fields = ['nome', 'classe', 'raca']