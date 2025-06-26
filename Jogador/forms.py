from .models import Jogador
from django.forms import ModelForm

class JogadorForm(ModelForm):
    class Meta: 
        model =  Jogador
        fields = ['nome', 'classe', 'raca', 'nivel', 'hp', 'guilda']