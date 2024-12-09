from django.db import models
from cliente.models import Cliente

class Compra(models.Model):
    STATUS_CHOICES = [
        ('PENDENTE', 'Pendente'),
        ('CONCLUIDA', 'Concluída'),
        ('CANCELADA', 'Cancelada'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True)
    valor_total = models.FloatField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDENTE')

    def __str__(self):
        return f"Compra #{self.id} - {self.cliente.nome} ({self.status})"
