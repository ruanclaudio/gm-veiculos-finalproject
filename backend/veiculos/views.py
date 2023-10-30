from decimal import Decimal
from .models import InteresseCompra, InteresseVenda, Veiculo, Modelo, Marca
from .serializers import *

from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import request, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView

"""
{
    {
        "id": 1,  // O ID será gerado automaticamente no banco de dados
        "nome": "Nome do Cliente",
        "telefone": "1234567890",
        "email": "cliente@example.com",
        "mensagem": "Mensagem de interesse na compra de um veículo.",
        "veiculo_id": 1  // Substitua pelo ID do veículo ao qual o interesse está relacionado
    }
}
"""

class FormulariosView(APIView):
    serializer_class = VeiculoSerializer

    '''
    def get(self, request, *args, **kwargs):
        form_type = request.data.get('form_type')
        if form_type == 'compra':
            form_compras = InteresseCompra.objects.all()
            serializer_compras = InteresseCompraSerializer(form_compras)
            return Response(serializer_compras.data)
        elif form_type == 'venda':
            form_vendas = InteresseVenda.objects.all()
            serializer_vendas = InteresseVendaSerializer(form_vendas, many=True)
            return Response(serializer_vendas.data)
    '''

    def post(self, request, *args, **kwargs):
        form_type = request.data.get('form_type')
        if form_type == 'compra':
            return self.post_form_compra(request)
        elif form_type == 'venda':
            return self.post_form_venda(request)
        else:
            return JsonResponse({'mensagem': 'Tipo de formulário inválido.'}, status=400)
    
    def post_form_compra(self, request, form_type):
        if form_type == 'compra':
            nome = request.data.get('nome')
            telefone = request.data.get('telefone')
            email = request.data.get('email')
            mensagem = request.data.get('mensagem')
            veiculo_id = request.data.get('veiculo')
            
            if veiculo_id is not None:
                try:
                    veiculo = Veiculo.objects.get(pk=veiculo_id)
                except Veiculo.DoesNotExist:
                    return JsonResponse({'mensagem': 'Veículo não encontrado.'}, status=400)
            else:
                veiculo = None
            
            interesse = InteresseCompra(nome=nome, telefone=telefone, email=email, mensagem=mensagem, veiculo=veiculo)
            interesse.save()
            
            return JsonResponse({'mensagem': 'Interesse de compra registrado com sucesso!'})
        else:
            return JsonResponse({'mensagem': 'Apenas solicitações POST são suportadas.'}, status=405)

    def post_form_venda(self, request):
        return Response(status=201)  # Retorna uma resposta vazia com status 201 (Created)


def get_filtro(request, filtro):
    if request.method == 'GET':
        if filtro == 'modelos':
            modelo = Modelo.objects.all()
            serializer = FiltroModeloSerializer(modelo, many=True)
            return JsonResponse(serializer.data, safe=False)
        
        elif filtro == 'marcas':
            marca = Marca.objects.all()
            serializer = FiltroMarcaSerializer(marca, many=True)
            return JsonResponse(serializer.data, safe=False)

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
    
        """
        def get_queryset(self):
            veiculos = Veiculo.objects.all()

            veiculos = self.filtrar_por_tipo(veiculos)
            veiculos = self.filtrar_por_faixa_de_preco(veiculos)
            veiculos = self.filtrar_por_marca(veiculos)
            veiculos = self.filtrar_por_modelo(veiculos)
            veiculos = self.filtrar_por_estado_usado(veiculos)
            veiculos = self.filtrar_por_leiloado(veiculos)

            veiculos = self.ordenar(veiculos)

            return veiculos
        """

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        
        return Response(serializer.data)
    
"""
def filtrar_por_tipo(self, queryset):
    tipo = self.request.query_params.get('tipo')
    if tipo:
        return queryset.filter(modelo__tipo=tipo)
    return queryset

def filtrar_por_faixa_de_preco(self, queryset):
    faixa_preco = self.request.query_params.get('preco')
    if faixa_preco:
        min_price, max_price = self.get_faixa_preco(faixa_preco)
        return queryset.filter(preco__gt=min_price, preco__lte=max_price)
    return queryset

def filtrar_por_marca(self, queryset):
    marca = self.request.query_params.get('marca')
    if marca:
        return queryset.filter(modelo__marca__nome=marca)
    return queryset

def filtrar_por_modelo(self, queryset):
    modelo = self.request.query_params.get('modelo')
    if modelo:
        return queryset.filter(modelo__nome=modelo)
    return queryset

def filtrar_por_estado_usado(self, queryset):
    estado_usado = self.request.query_params.get('usado')
    if estado_usado:
        return queryset.filter(condicao__condicao_usado=estado_usado)
    return queryset

def filtrar_por_leiloado(self, queryset):
    leiloado = self.request.query_params.get('leilao')
    if leiloado:
        return queryset.filter(condicao__leiloado=leiloado)
    return queryset

def ordenar(self, queryset):
    sort = self.request.query_params.get('sort')
    if sort == 'asc':
        return queryset.order_by('preco')
    elif sort == 'des':
        return queryset.order_by('-preco')
    return queryset

"""