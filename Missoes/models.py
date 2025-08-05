from django.db import models
from Personagem.models import Personagem

class Missao(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    recompensa = models.CharField(max_length=100)
    personagem = models.ForeignKey(Personagem, on_delete=models.CASCADE)
    concluida = models.BooleanField(default=False)

    class Meta:
        db_table = "missao_missoes"
        permissions = [
            ("detail_missao", "Pode ver o detalhe da missao"),
        ]

    def __str__(self):
        return self.titulo

