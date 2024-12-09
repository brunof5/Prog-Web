from django.db import models
from compras.models import Compra
from produtos.models import Produto

class ItensCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='itens')
    quantidade = models.PositiveIntegerField()
    preco_unitario = models.FloatField()

    def __str__(self):
        return f"Item_Compra: {self.produto.nome} (Compra #{self.compra.id}, Item #{self.produto.id})"

    def calcular_total(self):
        return self.quantidade * self.preco_unitario
