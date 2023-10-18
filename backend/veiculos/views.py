from .models import *
from .serializers import VeiculoSerializer

from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

class VeiculosList(ListAPIView):
    serializer_class = VeiculoSerializer

    def get_queryset(self):
        veiculos = Veiculos.objects.all()
        tipo = self.request.query_params.get('type')
        menor_preco = self.request.query_params.get('lowest_price')
        maior_preco = self.request.query_params.get('biggest_price')
        marca = self.request.query_params.get('brand')
        modelo = self.request.query_params.get('model')
        quilometragem = self.request.query_params.get('milage')
        novo = self.request.query_params.get('new')
        leilao = self.request.query_params.get('auction')

        if tipo is not None:
            veiculos = veiculos.filter(modelo__tipo=tipo)

        if menor_preco is not None:
            veiculos = veiculos.filter(preco__gt=menor_preco)

        if maior_preco is not None:
            veiculos = veiculos.filter(preco__lt=maior_preco)

        if marca is not None:
            veiculos = veiculos.filter(modelo__marca__nome=marca)

        if modelo is not None:
            veiculos = veiculos.filter(modelo__nome=modelo)

        if quilometragem is not None:
            veiculos = veiculos.filter(condicao__quilometragem__lt=quilometragem)

        if novo is not None:
            veiculos = veiculos.filter(condicao__condicao=novo)

        if leilao is not None:
            veiculos = veiculos.filter(condicao__leilao=leilao)

        return veiculos


    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)