from decimal import Decimal
from .models import InteresseCompra, InteresseVenda, Veiculo
from .serializers import VeiculoSerializer

from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import request, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

def receber_interesse_venda(request):
    if request.method == 'POST':
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        mensagem = request.POST.get('mensagem')
        
        interesse = InteresseVenda(telefone=telefone, email=email, mensagem=mensagem)
        interesse.save()
        
        return JsonResponse({'mensagem': 'Interesse de venda registrado com sucesso!'})
    else:
        return JsonResponse({'mensagem': 'Apenas solicitações POST são suportadas.'})
    
def receber_interesse_compra(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        mensagem = request.POST.get('mensagem')
        veiculo = request.POST.get('veiculo')
        
        interesse = InteresseCompra(nome = nome, telefone=telefone, 
                                    email=email, mensagem=mensagem, veiculo = veiculo)
        interesse.save()
        
        return JsonResponse({'mensagem': 'Interesse de venda registrado com sucesso!'})
    else:
        return JsonResponse({'mensagem': 'Apenas solicitações POST são suportadas.'})

class VeiculosList(ListAPIView):
    serializer_class = VeiculoSerializer

    def get_veiculo(self, veic_id):
        veiculo = Veiculo.objects.filter(id=veic_id)
        serializer = VeiculoSerializer(veiculo, many=True)
        return JsonResponse(serializer.data, safe=False)

    @staticmethod
    def get_faixa_preco(faixa_preco):
        min_price = None
        max_price = None

        if faixa_preco == 'a20':
            min_price = 0
            max_price = 20000
        if faixa_preco == 'a40':
            min_price = 20000
            max_price = 40000
        if faixa_preco == 'a60':
            min_price = 40000
            max_price = 60000
        if faixa_preco == 'a80':
            min_price = 60000
            max_price = 80000
        if faixa_preco == 'a100':
            min_price = 80000
            max_price = 100000
        if faixa_preco == 'm100':
            min_price = 100000
            max_price = 999999999

        return min_price, max_price

    def get_queryset(self):
        veiculos = Veiculo.objects.all()
        tipo = self.request.query_params.get('tipo') # carro ou moto
        faixa_preco = self.request.query_params.get('preco') # a20, a40, a60, a80, a100, m100
        marca = self.request.query_params.get('marca') # ex: honda
        modelo = self.request.query_params.get('modelo') # ex: civic
        estado_usado = self.request.query_params.get('usado') # True para usado
        leiloado = self.request.query_params.get('leilao') # true para leiloado
        sort = self.request.query_params.get('sort') # asc, des # padrao asc

        if faixa_preco is not None:
            min_price, max_price = self.get_faixa_preco(faixa_preco)
            veiculos = veiculos.filter(preco__gt=min_price, preco__lte=max_price)

        if tipo is not None:
            veiculos = veiculos.filter(modelo__tipo=tipo)

        if marca is not None:
            veiculos = veiculos.filter(modelo__marca__nome=marca)

        if modelo is not None:
            veiculos = veiculos.filter(modelo__nome=modelo)

        if estado_usado is not None:
            veiculos = veiculos.filter(condicao__condicao_usado=estado_usado)

        if leiloado is not None:
            veiculos = veiculos.filter(condicao__leiloado=leiloado)

        if sort == 'asc':
            veiculos = veiculos.order_by('preco')  # Ordene em ordem ascendente.
        elif sort == 'des':
            veiculos = veiculos.order_by('-preco')  # Ordene em ordem descendente.

        return veiculos

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        
        return Response(serializer.data)