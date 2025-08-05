from django.db import models

class Efeito(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    duracao = models.CharField(max_length=50, blank=True)  # Ex: “3 turnos”, “1 dia”

    class Meta:
        db_table = "Efeito_efeitos"
        permissions = [
            ("detail_efeitos", "Pode ver o detalhe de efeito"),
        ]

    def __str__(self):
        return self.nome
