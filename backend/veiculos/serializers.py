from .models import *
from rest_framework import serializers 

class CondicaoVeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CondicaoVeiculo
        fields = ['condicao_usado', 'ano', 'leiloado']

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = '__all__'
    
class ModeloSerializer(serializers.ModelSerializer):
    marca = serializers.StringRelatedField()

    class Meta:
        model = Modelo
        fields = ['nome', 'tipo', 'marca']

class VeiculoSerializer(serializers.ModelSerializer):
    modelo = ModeloSerializer()
    condicao = CondicaoVeiculoSerializer()

    class Meta:
        model = Veiculo
        fields = '__all__'