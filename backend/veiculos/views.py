from .models import *
from .serializers import *

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def veiculos_list(request):
    veiculos = Veiculos.objects.all()
    serializer = VeiculoSerializer(veiculos, many = True)
    return Response(serializer.data)