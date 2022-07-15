from statistics import mode
from django.db import models

# Create your models here.

class Tarefas(models.Model):

    nome = models.CharField(
        verbose_name='nome da task',
        max_length= 32
    )

    descriçao = models.TextField(
        verbose_name='Descrição',
        max_length=256,
    )

    prioridade = models.ForeignKey(
        'Prioridade',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    imagem = models.URLField(
        verbose_name='Imagem',
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.nome

    def get_nome(self):
        if self.nome:
            return self.nome
        else:
            return 'SEM NOME '

class Prioridade(models.Model):
    nivel = models.CharField(
        max_length=8,
        verbose_name='nivel de prioridade da tarefa'
    )
    def __str__(self):
        return self.nivel

