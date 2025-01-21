from django.db import models
from cliente.models import Cliente
from django.core.exceptions import ValidationError, ObjectDoesNotExist

class Compra(models.Model):
    STATUS_CHOICES = [
        ('PENDENTE', 'Pendente'),
        ('CONCLUIDA', 'Concluída'),
        ('CANCELADA', 'Cancelada'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True)
    valor_total = models.FloatField(default=0.0)   # TODO: valor total não aparece adequadamente
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDENTE')

    def __str__(self):
        return f"#{self.id} - {self.cliente.nome} ({self.status})"
    
    def save(self, *args, **kwargs):
        if self.pk:
            original = Compra.objects.get(pk=self.pk)
            if original.status in ['CONCLUIDA', 'CANCELADA']:
                raise ValidationError(f"Compras com status '{original.status}' não podem ser alteradas.")
            if original.data != self.data:
                raise ValidationError("A data de compra não pode ser alterada")

        if self.status == "CONCLUIDA":
            try:
                if not self.pagamento or self.pagamento.status != "PAGO":
                    raise ValidationError("Uma compra só pode ser concluída se o pagamento estiver 'Pago'.")
            except ObjectDoesNotExist:
                    raise ValidationError("Não é possível concluir a compra sem um pagamento associado.")

        if self.status == "CONCLUIDA":
            for item in self.itenscompra.all():
                if item.produto.estoque >= item.quantidade:
                    item.produto.estoque -= item.quantidade
                    item.produto.save()
                else:
                    raise ValidationError(f"Estoque insuficiente para {item.produto.nome}.")
                    
        super().save(*args, **kwargs)

    def atualizar_valor_total(self):
        total = sum(item.quantidade * item.preco_unitario for item in self.itenscompra.all())
        self.valor_total = total
        self.save(update_fields=['valor_total'])
