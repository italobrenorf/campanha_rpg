from django.db import models


class Npc(models.Model):
    nome = models.CharField(max_length=100)
    classe = models.CharField(max_length=50)
    raca = models.CharField(max_length=50)
    descricao = models.TextField(blank=True, null=True)
    
    class Meta:
        db_table = "Npc_npcs"
        permissions = [
            ("detail_npc", "Pode ver o detalhe do npc"),
        ]

    def __str__(self):
        return self.nome