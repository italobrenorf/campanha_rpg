from django.db import models

class Guilda(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        db_table = "Guilda_guildas"
        permissions = [
            ("detail_guilda", "Pode ver o detalhe da guilda"),
        ]

    def __str__(self):
        return self.nome