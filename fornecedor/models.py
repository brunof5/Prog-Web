from django.db import models

class Fornecedor(models.Model):
    nome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"Fornecedor #{self.id} - {self.nome}"