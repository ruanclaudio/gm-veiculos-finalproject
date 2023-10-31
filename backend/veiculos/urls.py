from django.urls import re_path, path

from .views import VeiculosList, FormCompraView, FormVendaView, receber_interesse_venda, receber_interesse_compra, get_filtro

urlpatterns = [
     re_path(r'^(?P<veic_id>\w+)$', VeiculosList.get_veiculo, name='get-veiculo'),
     re_path(r'^$', VeiculosList.as_view(), name='veiculos-list'),
     path("form-compra/", FormCompraView.as_view(), name="form-compra"),
     path("form-venda/", FormVendaView.as_view(), name="form-venda"),
     re_path(r'^filtros/(?P<filtro>\w+)$', get_filtro, name='get-filtro'),
]

