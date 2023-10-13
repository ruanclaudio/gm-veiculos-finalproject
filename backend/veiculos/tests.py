from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Veiculos
from .serializers import VeiculoSerializers

class VeiculosListTest(TestCase):
    def setUp(self):
        for i in range(15):
            Veiculos.objects.create(preco=10000, pagamento='À vista')

    def test_paginacao(self):
        client = APIClient()
        url = reverse('veiculos_list')

        response = client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 10)  # verifique se a página 1 retorna 10 veiculos

        response = client.get(url, {'page': 2})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 10)  # verifique se a página 2 retorna 10 veiculos