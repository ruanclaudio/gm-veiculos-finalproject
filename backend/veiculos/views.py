from .models import *
from .serializers import *

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.paginator import Paginator

@api_view(['GET'])
def veiculos_list(request):
    # serializa todos os veiculos
    veiculos = Veiculos.objects.all()
    serializer = VeiculoSerializer(veiculos, many = True)

    # faz a paginacao
    paginator = Paginator(veiculos, 10)
    
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return Response(serializer.data)