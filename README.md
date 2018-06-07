# Projeto

###### Desenvolvendo uma API RESTful com Django Framework
###### Criação de um projeto de API de Pontos Turísticos

### RESTful Web API para exposição de pontos turísticos de uma região
* Propo um novo ponto turístico
* Moderação dos pontos turísticos cadastrados
* Listagem básica dos pontos turísticos (lista reumida)
* Listagem completa dos pontos turísticos
* Detalhe de um ponto turísticos
* Atualização de um ponto turísticos por usuários autorizados
* Deleção de um ponto turísticos por usuários autorizados

#### Preparação do ambiente
* Python 3.6.4 (my 3.6.5)
* Pycharm
* venv
* Django 2.0.4 (my 2.0.5)

###### Package   Version
* Django 2.0.5
* djangorestframework 3.8.2
* pip 10.0.1
* pytz 2018.4
* setuptools 28.80
* pillow 5.1.0

#### Deploy no Heroku

###### Regra de Negócio
* Propor um novo ponto turístico - Qualquer pessoa
* Moderação dos p-t cadastrados - Adm da API
* Listagem básica dos p-t (lista resumida) - Via token
* Listagem completa dos p-t - Via token
* Detalhe de um p-t Via token
* Atualização de um p-t somente usuaŕios autorizados - Via token (permissão especial)
* Deleção de um p-t por usuáriosi autorizados - Via token (permissão especial)e

###### Apps
* Atração ------> Ponto turístico---->Localização 
* Ponto turísitico <------ Comentários<-------Users


# Start

##Criando e modelando a app

#### Instalação do Django
###### Cria o virtual env
* $ python -m venv venv

###### Instala o Django
* $ pip install django

###### Criando o projeto
* $ django-admin.py startproject nome_projeto .

###### Cria o database
* $ python manage.py migrate

###### Uma view rápida no projeto
* $ python manage.py runserver

###### Cria uma app
* $ python manage.py startapp new_nome_app

#### Criar uma pasta dentro de new_nome_app de nome api
###### Criar em seguida os arquivos
* serializers.py
* viewsets.py

###### Definindo um model


```
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

    def __str__(self):
        return self.nome
```
###### Ativando o model
```

INSTALLED_APPS = [
    ...
    
    'django.contrib.staticfiles',
    'rest_framework',
    #my_apps
    'core',
    'atracoes',
    'comentarios',
    'avaliacoes',
    'localizacoes', # = enderecos
]
```
###### Migrando o database
* $ python manage.py makemigrations
* $ python manage.py migrate
###### Criando o Superuser
* $ python manage.py createsuperuser

###### Registrando o model em admin.py
```
from django.contrib import admin
from .models import PontoTuristico

admin.site.register(PontoTuristico)
```
###### viewsets.py
```
from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):
    queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer
```
###### serializers.py
```
from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico


class PontoTuristicoSerializer(ModelSerializer):
    class Meta:
        model = PontoTuristico
        fields = (
            'id',
            'nome',
            'descricao'
        )
```
###### Configurando a URL
```
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from core.api.viewsets import PontoTuristicoViewSet

router = routers.DefaultRouter()
router.register(r'pontosturisticos', PontoTuristicoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
```
## Criando o EndPoint

#### Incluir em urls.py 
```
from atracoes.api.viewsets import AtracoesViewSet #EndPoint

router = routers.DefaultRouter()
router.register(r'pontosturisticos', PontoTuristicoViewSet)
router.register(r'atracoes', AtracoesViewSet) #EndPoint
```

#### Configurar os serializers.py e viewsets.py
* conforme passos anteriormente mostrados

