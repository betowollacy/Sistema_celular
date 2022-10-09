from tabnanny import verbose
from django.db import models
from datetime import date
from usuarios.models import Usuario

class Categoria(models.Model):
    nome = models.CharField(max_length = 30)
    descricao = models.TextField()

    def __str__(self):
        return self.nome   

class Aparelhos(models.Model):
    nome_cliente = models.CharField(max_length=100)
    contato = models.CharField(max_length=11)
    modelo_aparelho = models.CharField(max_length=30)
    defeito_informado = models.TextField(max_length=255, blank = True, null=True)
    data_entrada = models.DateField(default=date.today)
    data_saida = models.DateTimeField(blank = True, null=True)
    status_servico = models.BooleanField(default=False)
    nome_retirada = models.CharField(max_length=30, blank = True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'aparelho'

    def __str__(self):
        return self.nome_cliente     

    