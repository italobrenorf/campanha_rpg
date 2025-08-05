from .models import Personagem
from django.forms import ModelForm

class PersonagemForm(ModelForm):
    class Meta: 
        model =  Personagem
        fields = ['user','nome', 'classe', 'raca', 'nivel', 'hp', 'ouro', 'guilda', 'historia']
        labels = {
            'user': 'Jogador',
        }