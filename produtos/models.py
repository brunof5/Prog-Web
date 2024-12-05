from django.db import models
from fornecedor.models import Fornecedor

class Produto(models.Model):
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    valor = models.FloatField()
    descricao = models.TextField()
    estoque = models.PositiveIntegerField()
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
