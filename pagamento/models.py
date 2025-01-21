from django.db import models
from compras.models import Compra
from django.core.exceptions import ValidationError

class Pagamento(models.Model):
    compra = models.OneToOneField(Compra, on_delete=models.CASCADE, related_name='pagamento')
    metodo = models.CharField(max_length=50, choices=[
        ('CARTAO_CREDITO', 'Cartão de Crédito'),
        ('BOLETO', 'Boleto'),
        ('PIX', 'PIX'),
        ('TRANSFERENCIA', 'Transferência Bancária'),
    ])
    data_pagamento = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('PENDENTE', 'Pendente'),
        ('PAGO', 'Pago'),
        ('CANCELADO', 'Cancelado'),
    ])

    def __str__(self):
        return f"Pagamento da Compra #{self.compra.id} - {self.metodo} - Status: {self.status}"
    
    def save(self, *args, **kwargs):
        if self.pk:
            original = Pagamento.objects.get(pk=self.pk)
            if original.status in ['PAGO', 'CANCELADO']:
                raise ValidationError(f"Pagamentos com status '{original.status}' não podem ser alterados.")
            if original.data_pagamento != self.data_pagamento:
                raise ValidationError("A data de pagamento não pode ser alterada.")
            
        if self.compra.status != "PENDENTE":
            raise ValidationError("Um pagamento só pode ser adicionado a uma compra com status 'Pendente'.")

        super().save(*args, **kwargs)
