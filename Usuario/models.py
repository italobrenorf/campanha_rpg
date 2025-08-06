from django.db import models
from django.contrib.auth.models import User

class Usuario(User):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    telefone = models.IntegerField()

    class Meta:
        db_table = "Usuario_usuarios"
        permissions = [
            ("detail_usuario", "Pode ver o detalhe de usuario"),
        ]

    def __str__(self):
        return self.nome
