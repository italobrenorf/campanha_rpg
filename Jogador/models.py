from django.db import models
from Guilda.models import Guilda

class Jogador(models.Model):
    nome = models.CharField(max_length=100)
    classe = models.CharField(max_length=50)
    raca = models.CharField(max_length=50)
    nivel = models.IntegerField()
    hp = models.IntegerField()
    guilda = models.ForeignKey(Guilda, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = "Jogador_jogadores"
        permissions = [
            ("detail_jogador", "Pode ver o detalhe de jogador"),
        ]

    def __str__(self):
        return self.nome