# Projeto

## Criação de um projeto de API de Pontos Turísticos

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

#### Deploy no Heroku

### Regra de Negócio
* Propor um novo ponto turístico - Qualquer pessoa
* Moderação dos p-t cadastrados - Adm da API
* Listagem básica dos p-t (lista resumida) - Via token
* Listagem completa dos p-t - Via token
* Detalhe de um p-t Via token
* Atualização de um p-t somente usuaŕios autorizados - Via token (permissão especial)
* Deleção de um p-t por usuáriosi autorizados - Via token (permissão especial)e

#### Apps
* Atração ------> Ponto turístico---->Localização 
* Ponto turísitico <------ Comentários<-------Users