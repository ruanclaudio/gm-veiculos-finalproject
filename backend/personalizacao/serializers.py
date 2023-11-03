from .models import *
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


class PromocaoSerializer(ModelSerializer):
    class Meta:
        model = Promocao
        fields = ['imagem_banner'] #  "__all__"