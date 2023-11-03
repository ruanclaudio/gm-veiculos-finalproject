from django.shortcuts import render

from .models import *
from .serializers import *

from rest_framework.generics import ListAPIView

class PromocaoList(ListAPIView):
    serializer_class = PromocaoSerializer

    def get_queryset(self):
        user = self.request.user
        return Promocao.objects.filter(ativa=True)