from django.db import models
from compras.models import Compra
from produtos.models import Produto
from django.core.exceptions import ValidationError

class ItensCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name='itenscompra')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    preco_unitario = models.FloatField()

    def __str__(self):
        return self.produto.nome

    def save(self, *args, **kwargs):
        self.preco_unitario = self.produto.valor
        if self.quantidade > self.produto.estoque:
            raise ValidationError("A quantidade não pode ultrapassar o estoque disponível.")
        if not self.produto.disponivel:
            raise ValidationError("O produto selecionado não está disponível.")
        super().save(*args, **kwargs)
        self.compra.atualizar_valor_total()

    def clean(self):
        super().clean()
        if not self.produto.disponivel:
            raise ValidationError("O produto selecionado não está disponível.")
        if self.quantidade > self.produto.estoque:
            raise ValidationError("A quantidade não pode ultrapassar o estoque disponível.")
        
    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        self.compra.atualizar_valor_total()
