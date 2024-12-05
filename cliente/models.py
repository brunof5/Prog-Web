from django.contrib.auth.models import User
from django.db import models

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    idade = models.IntegerField()
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username
