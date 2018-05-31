from django.db import models
from atracoes.models import Atracao


class PontoTuristico(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracao)

    def __str__(self):
        return self.nome


