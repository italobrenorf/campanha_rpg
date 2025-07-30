from django.db import models
from Guilda.models import Guilda

class Monstro(models.Model):
    raca = models.CharField(max_length=50)
    nivel = models.IntegerField()
    hp = models.IntegerField()

    class Meta:
        db_table = "Monstro_Monstros"
        permissions = [
            ("detail_Monstro", "Pode ver o detalhe de Monstro"),
        ]

    def __str__(self):
        return self.nome