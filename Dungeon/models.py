from django.db import models
from Guilda.models import Guilda

class Dungeon(models.Model):
    nome = models.CharField(max_length=100)
    nivelrecomendado = models.IntegerField()


    class Meta:
        db_table = "Dungeon_dungeons"
        permissions = [
            ("detail_dungeon", "Pode ver o detalhe de dungeon"),
        ]

    def __str__(self):
        return self.nome