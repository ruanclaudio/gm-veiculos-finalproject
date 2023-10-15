from .models import *
from rest_framework import serializers 

class CondicoeseiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CondicoesVeiculos
        fields = '__all__'

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marcas
        fields = '__all__'
    
class ModeloSerializer(serializers.ModelSerializer):
    marca = MarcaSerializer()

    class Meta:
        model = Modelos
        fields = '__all__'

class VeiculoSerializer(serializers.ModelSerializer):
    modelo = ModeloSerializer()
    condicao = CondicoeseiculoSerializer()

    class Meta:
        model = Veiculos
        fields = '__all__'