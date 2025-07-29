from .models import item
from django.forms import ModelForm

class ItemForm(ModelForm):
    class Meta: 
        model =  item
        fields = ['nome', 'tipo', 'valor']