from django.db import models


class Filme(models.Model):
    nome = models.CharField(max_length=256)
    diretor = models.CharField(max_length=256)
    ano = models.CharField(max_length=30)

    def __str__(self):
        return self.nome
