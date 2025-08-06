from .models import Personagem
from django.forms import ModelForm

class PersonagemForm(ModelForm):
    class Meta: 
        model =  Personagem
        fields = ['Usuario','nome', 'classe', 'raca', 'nivel', 'hp', 'ouro', 'guilda', 'historia']
        labels = {
            'Usuario': 'Jogador',
        }