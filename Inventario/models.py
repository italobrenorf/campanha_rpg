from django.db import models
from Personagem.models import Personagem
from Item.models import Item

class Inventario(models.Model):
    personagem = models.ForeignKey(Personagem, on_delete=models.CASCADE, related_name='inventario')
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=1)
    equipado = models.BooleanField(default=False)

    class Meta:
        db_table = "Inventario_inventarios"
        permissions = [
            ("detail_inventario", "Pode ver o detalhe de inventario"),
        ]