from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.

# Cada modelo Python(classe) é uma subclasse de models.Model
# E cada atributo da classe representa um campo na base de dados.


class Receita(models.Model):

    #  CRiando um relacionamento ente a classe pessoa com a classe receita --> Assim, o modleo receito tera uma pessoa
    pessoa = models.ForeignKey(User, on_delete=models.CASCADE)

    nome_receita = models.CharField(max_length=200)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    date_receita = models.DateTimeField(default=datetime.now, blank=True)

    # Quando for carregado uma imagem, ira Adicionar na pasta medias(criado pela rota especificada) a imagem no endereço
    foto_receita = models.ImageField(upload_to='fotos/%d/%m/%Y/', blank=True)

    publicada = models.BooleanField(default=False)

    def __str__(self):
        return self.nome_receita


# Ao adicionar uma modelo(classe) novo, o Django ira automaticamente executar o seguinte comando do banco de dados
"""
CREATE TABLE receitas_receita (
    "id" serial NOT NULL PRIMARY KEY,
    "first_name" varchar(30) NOT NULL,
    "last_name" varchar(30) NOT NULL
);
"""