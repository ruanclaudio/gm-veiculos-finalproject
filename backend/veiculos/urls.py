from django.urls import re_path

from .views import VeiculosList

urlpatterns = [
     re_path(r'^$', VeiculosList.as_view(), name='veiculos-list'),
]