from django.urls import re_path, path

from .views import VeiculosList, FormulariosView, receber_interesse_venda, receber_interesse_compra, get_filtro

urlpatterns = [
     re_path(r'^(?P<veic_id>\w+)$', VeiculosList.get_veiculo, name='get-veiculo'),
     re_path(r'^$', VeiculosList.as_view(), name='veiculos-list'),
     path("formularios/<str:form_type>/", FormulariosView.as_view(), name="formulario"),
     re_path(r'^filtros/(?P<filtro>\w+)$', get_filtro, name='get-filtro'),
]

