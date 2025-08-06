from .models import Usuario
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = [ 'nome', 'password1', 'password2', 'idade', 'telefone']

class UsuarioEditForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = [ 'nome', 'idade', 'telefone']
