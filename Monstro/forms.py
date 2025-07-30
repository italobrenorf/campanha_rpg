from .models import Monstro
from django.forms import ModelForm

class MonstroForm(ModelForm):
    class Meta: 
        model =  Monstro
        fields = ['nivel', 'hp','raca']