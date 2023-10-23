from .models import *
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

class CondicaoVeiculoSerializer(ModelSerializer):
    class Meta:
        model = CondicaoVeiculo
        fields = ['condicao_usado', 'ano', 'leiloado', 'quilometragem']

class MarcaSerializer(ModelSerializer):
    class Meta:
        model = Marca
        fields = '__all__'
    
class ModeloSerializer(ModelSerializer):
    marca = serializers.StringRelatedField()

    class Meta:
        model = Modelo
        fields = ['nome', 'tipo', 'marca']

class VeiculoSerializer(ModelSerializer):
    modelo = ModeloSerializer()
    condicao = CondicaoVeiculoSerializer()

    class Meta:
        model = Veiculo
        fields = '__all__'