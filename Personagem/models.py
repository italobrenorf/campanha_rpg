from django.db import models
from Guilda.models import Guilda
from Usuario.models import Usuario

class Personagem(models.Model):
    Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    classe = models.CharField(max_length=50)
    raca = models.CharField(max_length=50)
    nivel = models.IntegerField()
    hp = models.IntegerField()
    historia = models.TextField(blank=True)
    ouro = models.IntegerField(default=0)
    guilda = models.ForeignKey(Guilda, on_delete=models.SET_NULL, null=True, blank=True, related_name='membros')

    class Meta:
        db_table = "Personagem_personagens"
        permissions = [
            ("detail_personagem", "Pode ver o detalhe de personagem"),
        ]

    def __str__(self):
        return self.nome