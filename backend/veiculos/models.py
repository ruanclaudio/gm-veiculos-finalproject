# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CondicoesVeiculos(models.Model):
    condicao = models.CharField(max_length=25)
    ano = models.PositiveSmallIntegerField()
    cor = models.CharField(max_length=50)
    quilometragem = models.IntegerField()
    leilao = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'condicoes_veiculos'


class Marcas(models.Model):
    nome = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'marcas'


class Modelos(models.Model):
    nome = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    marca = models.ForeignKey(Marcas, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'modelos'


class Veiculos(models.Model):
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    pagamento = models.CharField(max_length=50)
    modelo = models.ForeignKey(Modelos, models.DO_NOTHING)
    condicao = models.ForeignKey(CondicoesVeiculos, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'veiculos'
