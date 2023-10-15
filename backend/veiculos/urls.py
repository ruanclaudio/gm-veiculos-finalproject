from django.urls import path

from . import views

urlpatterns = [
    path("", views.veiculos_list, name="veiculos_list"),
]