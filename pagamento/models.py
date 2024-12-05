from django.db import models
from compras.models import Compra

class Pagamento(models.Model):
    compra = models.OneToOneField(Compra, on_delete=models.CASCADE, related_name='pagamento')
    metodo = models.CharField(max_length=50, choices=[
        ('CARTAO_CREDITO', 'Cartão de Crédito'),
        ('BOLETO', 'Boleto'),
        ('PIX', 'PIX'),
        ('TRANSFERENCIA', 'Transferência Bancária'),
    ])
    data_pagamento = models.DateField()
    status = models.CharField(max_length=20, choices=[
        ('PENDENTE', 'Pendente'),
        ('PAGO', 'Pago'),
        ('CANCELADO', 'Cancelado'),
    ])

    def __str__(self):
        return f"Pagamento da Compra #{self.compra.id} - {self.metodo}"
