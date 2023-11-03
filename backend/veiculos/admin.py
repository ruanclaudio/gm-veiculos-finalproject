from django.contrib import admin
from .models import *
from django.utils.html import format_html
from django.urls import reverse

# Register your models here.
admin.site.register(CondicaoVeiculo)
admin.site.register(Marca)





class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('preco', 'pagamento', 'porcentagem_desconto',
                    'desconto_ativo', 'modelo', 'condicao', 'display_image', 'edit_modelo')

    def display_image(self, obj):
        return format_html('<img src="{}" style="max-width: 100px; max-height: 100px;" />', obj.imagem.url)

    display_image.short_description = 'Imagem'

    def edit_modelo(self, obj):
        edit_url = reverse("admin:veiculos_modelo_change", args=[obj.modelo.id])
        return format_html('<a href="{}" class="button" target="_blank">Editar Modelo</a>', edit_url)

    edit_modelo.short_description = 'Editar Modelo'

admin.site.register(Veiculo, VeiculoAdmin)



admin.site.register(InteresseCompra)
admin.site.register(InteresseVenda)