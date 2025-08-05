from django.db import models

class item(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)  # Ex: Arma, Poção, Armadura
    valor = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)  # Aceita casas decimais
    descricao = models.TextField(blank=True)

    class Meta:
        db_table = "item_itens"
        permissions = [
            ("detail_item", "Pode ver o detalhe do item"),
        ]

    def __str__(self):
        return self.nome
