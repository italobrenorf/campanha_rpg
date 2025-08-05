from django.db import models
from Personagem.models import Personagem

class Evento(models.Model):
    personagem = models.ForeignKey(Personagem, null=True, blank=True, on_delete=models.SET_NULL)
    descricao = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    tipo = models.CharField(max_length=50)  # Ex: “Combate”, “Missão”, “Exploração”

    class Meta:
        db_table = "Evento_eventos"
        permissions = [
            ("detail_eventos", "Pode ver o detalhe do evento"),
        ]

    def __str__(self):
        return f"{self.tipo} - {self.data.strftime('%d/%m/%Y')}"

