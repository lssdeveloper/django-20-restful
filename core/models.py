from django.db import models
from atracoes.models import Atracao
from comentarios.models import Comentario
from avaliacoes.models import Avaliacao
from localizacoes.models import Localizacao


class PontoTuristico(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracao)
    comentarios = models.ManyToManyField(Comentario)
    avaliacoes = models.ManyToManyField(Avaliacao)
    localizacao = models.ForeignKey(Localizacao, on_delete=models.CASCADE, null=True, blank=True)
    foto = models.ImageField(upload_to='pontos_turisticos', null=True, blank=True)


    def __str__(self):
        return self.nome


