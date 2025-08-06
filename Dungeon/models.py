from django.db import models

class Dungeon(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    nivel_minimo = models.IntegerField(default=1)


    class Meta:
        db_table = "Dungeon_dungeons"
        permissions = [
            ("detail_dungeon", "Pode ver o detalhe de dungeon"),
        ]

    def __str__(self):
        return self.nome