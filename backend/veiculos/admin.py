from django.contrib import admin
from .models import *
# Register your models here.

# Registre cada classe de modelo individualmente
admin.site.register(CondicoesVeiculos)
admin.site.register(Marcas)
admin.site.register(Modelos)
admin.site.register(Veiculos)
admin.site.register(InteresseCompra)
admin.site.register(InteresseVenda)