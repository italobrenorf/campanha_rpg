from .models import Missao
from django.forms import ModelForm

class MissaoForm(ModelForm):
    class Meta: 
        model =  Missao
        fields = ['titulo','descricao', 'recompensa', 'personagem', 'concluida']