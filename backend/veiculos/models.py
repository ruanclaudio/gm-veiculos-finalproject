from django.db import models


class CondicaoVeiculo(models.Model):
    condicao_usado = models.BooleanField() 
    ano = models.PositiveSmallIntegerField()  # PositiveSmallIntegerField para campo YEAR
    leiloado = models.BooleanField()
    quilometragem = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'condicoes_veiculos'


class Marca(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return (self.nome)

    class Meta:
        managed = False
        db_table = 'marcas'


class Modelo(models.Model):
    nome = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    marca = models.ForeignKey(Marca, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'modelos'


class Veiculo(models.Model):
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    pagamento = models.CharField(max_length=50)
    porcentagem_desconto = models.IntegerField()
    modelo = models.ForeignKey(Modelo, models.DO_NOTHING)
    condicao = models.ForeignKey(CondicaoVeiculo, models.DO_NOTHING)
    imagem = models.ImageField(upload_to="veiculos/")
    

    class Meta:
        managed = False
        db_table = 'veiculos'


"""
formularios de interesse de compra e venda
"""

class InteresseCompra(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=11)
    email = models.CharField(max_length=150)
    mensagem = models.CharField(max_length=1000)
    estado = models.CharField(max_length=50, default='Não Analisado')
    veiculo = models.ForeignKey('Veiculo', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'interesse_compra'


class InteresseVenda(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=11)
    email = models.CharField(max_length=150)
    mensagem = models.CharField(max_length=1000)
    imagem = models.ImageField(upload_to="veiculos/interesse_venda/")
    
    class Meta:
        managed = False
        db_table = 'interesse_venda'