from django.urls import re_path, path

from .views import PromocaoList

urlpatterns = [
     path("promocoes/", PromocaoList.as_view(), name="promo-list"),
]