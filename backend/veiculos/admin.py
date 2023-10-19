from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(CondicaoVeiculo)
admin.site.register(Marca)
admin.site.register(Modelo)
admin.site.register(Veiculo)
admin.site.register(InteresseCompra)
admin.site.register(InteresseVenda)