from .models import npc
from django.forms import ModelForm

class NpcForm(ModelForm):
    class Meta: 
        model =  npc
        fields = ['nome', 'classe', 'raca']