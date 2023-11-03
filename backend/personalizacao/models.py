from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

class Promocao(models.Model):
    nome = models.CharField(max_length=50)
    imagem_banner = models.ImageField(upload_to="banners/")
    ativa = models.BooleanField(default=False)

    class Meta:
        managed = False
        db_table = 'promocoes'

    def definir_como_ativa(self):
        Promocao.objects.exclude(pk=self.pk).update(ativa=False)
        self.ativa = True


"""
signais
"""

@receiver(pre_save, sender=Promocao)
def definir_promocao_ativa(sender, instance, **kwargs):
    """
    sempre que selecionar uma promcoao como ativa desmarca o campo ativo de todas as outras
    """
    if instance.ativa:
        instance.definir_como_ativa()
