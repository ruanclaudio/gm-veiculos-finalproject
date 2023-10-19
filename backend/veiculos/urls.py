from django.urls import re_path, path

from .views import VeiculosList, receber_interesse_venda, receber_interesse_compra

urlpatterns = [
     re_path(r'^(?P<veic_id>\w+)$', VeiculosList.get_veiculo, name='get-veiculo'),
     re_path(r'^$', VeiculosList.as_view(), name='veiculos-list'),
     path("interesse-venda/", receber_interesse_venda, name="interesse-venda"),
     path("interesse-compra/", receber_interesse_compra, name="interesse-compra"),
]

