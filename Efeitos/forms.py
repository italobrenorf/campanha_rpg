from .models import Efeito
from django.forms import ModelForm

class EfeitoForm(ModelForm):
    class Meta: 
        model =  Efeito
        fields = ['nome','descricao', 'duracao']