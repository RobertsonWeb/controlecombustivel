from datetime import datetime

from django.db import models
from django.urls import reverse


class AbastecimentoKmPendenteManager(models.Manager):
    def get_queryset(self):
        return super(AbastecimentoKmPendenteManager, self).get_queryset().filter(km_percorridos__isnull=True)


class AbastecimentoSomatorioValorMesAnterior(models.Manager):
    def get_queryset(self):
        if datetime.now().month == 1:
            mes_anterior = 12
            ano = datetime.now().year - 1
        else:
            mes_anterior = datetime.now().month - 1
            ano = datetime.now().year
        return super(AbastecimentoSomatorioValorMesAnterior, self).get_queryset().filter(data__year=ano, data__month=mes_anterior).aggregate(valor_total=models.Sum('valor'), valor_media=models.Avg('valor'))


class AbastecimentoSomatorioValorMesVigente(models.Manager):
    def get_queryset(self):
        return super(AbastecimentoSomatorioValorMesVigente, self).get_queryset().filter(data__year=datetime.now().year, data__month=datetime.now().month).aggregate(valor_total=models.Sum('valor'), valor_media=models.Avg('valor'))


class Abastecimento(models.Model):
    TIPOS_COMBUSTIVEL = (
        ('GASOLINA', 'Gasolina'),
        ('ETANOL', 'Etanol'),
        ('GNV', 'GNV'),
        ('DIESEL', 'Diesel'),
    )
    data = models.DateField('Data')
    posto = models.CharField('Posto', max_length=40)
    tipo_combustivel = models.CharField('Tipo do combustível', max_length=10, choices=TIPOS_COMBUSTIVEL, default='GASOLINA')
    litros = models.DecimalField('Litros', max_digits=10, decimal_places=2)
    valor = models.DecimalField('Valor', max_digits=10, decimal_places=2)
    km_percorridos = models.DecimalField('Km percorridos', max_digits=10, decimal_places=2, blank=True, null=True)
    km_media_por_litro = models.DecimalField('Km percorridos', max_digits=10, decimal_places=2, default=0)

    objects = models.Manager()
    km_pendente = AbastecimentoKmPendenteManager()
    mes_anterior = AbastecimentoSomatorioValorMesAnterior()
    mes_vigente = AbastecimentoSomatorioValorMesVigente()


    class Meta:
        ordering  =  ['data']

    def __str__(self):
        return '%s - %s' % (self.data.strftime('%d/%m/%Y'), self.posto)

    @property
    def valor_litro(self):
        return self.valor/self.litros

    @property
    def get_absolute_url(self):
        return reverse('abastecimento_change', args=[str(self.id)])

    @property
    def get_informar_km_percorrida_url(self):
        return reverse('abastecimento_km_percorrida', args=[str(self.id)])

    @property
    def get_delete_url(self):
        return reverse('abastecimento_delete', args=[str(self.id)])

    def save(self, *args, **kwargs):
        if self.km_percorridos:
            self.km_media_por_litro = self.km_percorridos/self.litros
        super(Abastecimento, self).save(*args, **kwargs)
