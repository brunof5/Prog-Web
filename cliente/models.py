from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    idade = models.IntegerField()
    endereco = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return f"Cliente #{self.id} - {self.nome}"
