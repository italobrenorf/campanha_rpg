from .models import Dungeon
from django.forms import ModelForm

class DungeonForm(ModelForm):
    class Meta: 
        model =  Dungeon
        fields = ['nome', 'nivelrecomendado']