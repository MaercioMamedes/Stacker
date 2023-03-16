# Staker
## Gerenciador de pátio automotivo

Esse projeto é uma API web que gerencia o controle logístico de uma frota num pátio de centro
de distribuíção de automóveis. Como premissas para resolução do problema, a movimentação dos carros
nesse pátio, acontece numa estrututura de pilha, onde o primeiro carro estacionado é o último a
sair.

A motivação desse projeto, é desenvolver uma solução cuja a solução seja baseada numa estrutura de dados do tipo pilha,
e a forma de autenticação das requisições utilize uma API Key

## Building

Esse projeto foi desenvolvido utilizando a versão 3.2.6 do interpretador Python. Todas as dependências
estão listadas no arquivo *requiments.txt*

### Como rodar ?

* realize o clone do repositório - `git clone https://github.com/MaercioMamedes/Stacker.git`
* [crie um ambiente virtual dentro do diretório do projeto e instale todas as dependências](https://www.alura.com.br/artigos/ambientes-virtuais-em-python)
* rode o comando `python manage.py runserver`

### End points

|         URI          |    MÉTODO    |            RECURSO             |
|:--------------------:|:------------:|:------------------------------:|
|          /           |     GET      | lista pilha de carros no pátio |
|    /inserir-carro    |     POST     |   insere novo carro na pilha   |
|    /remover-carro    |     GET      |     remove carro da pilha      |


## Chave de atenticação para acesso aos recursos da API
key = 03UcxXXH.knfewHj1FR83DAIwq49GAASQpsHR2vuM

## Criando uma API key
* Acesso modo terminal do django: `python manage.py shell`
* importe a classe APIKey:`from rest_framework_api_key.models import APIKey`
* Crie gere uma chave uma instância da classe APIKey: `api_key, key = APIKey.objects.create_key(name="my-remote-service")`

## parâmetros para adicionar carro à pilha

`{
    "brand": "marca do carro",
    "model": "modelo do carro",
    "color": "cor do carro",
    "license_plate": "placa do carro"
}`