from .models import *
from rest_framework import serializers 

class CondicaoVeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CondicaoVeiculo
        fields = '__all__'

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = '__all__'
    
class ModeloSerializer(serializers.ModelSerializer):
    marca = MarcaSerializer()

    class Meta:
        model = Modelo
        fields = '__all__'

class VeiculoSerializer(serializers.ModelSerializer):
    modelo = ModeloSerializer()
    condicao = CondicaoVeiculoSerializer()

    class Meta:
        model = Veiculo
        fields = '__all__'