from django.contrib import admin
from .models import *
from django.utils.html import format_html
from django.urls import reverse

# Register your models here.
admin.site.register(CondicaoVeiculo)
admin.site.register(Marca)
admin.site.register(Modelo)
admin.site.register(InteresseCompra)
admin.site.register(InteresseVenda)

class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('preco', 'pagamento', 'porcentagem_desconto',
                    'desconto_ativo', 'modelo',
                    'condicao', 'display_image')  # Adiciona 'display_image' à lista

    def display_image(self, obj):
        return format_html('<img src="{}" width="150" height="50" />', obj.imagem.url)

    display_image.short_description = 'Imagem'  # Nome da coluna na tabela

admin.site.register(Veiculo, VeiculoAdmin)