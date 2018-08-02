from django.shortcuts import render
from django.views.generic.base import TemplateView

from abastecimento.models import Abastecimento


class PainelView(TemplateView):
    template_name = 'core/painel.html'

    def get_context_data(self, **kwargs):

        valor_total_mes_anterior = Abastecimento.mes_anterior.all()['valor_total']
        valor_total_mes_vigente = Abastecimento.mes_vigente.all()['valor_total']
        diferenca_valores_totais = valor_total_mes_anterior - valor_total_mes_vigente

        context = super(PainelView, self).get_context_data(**kwargs)
        context.update({'abastecimentos_km_pendente': Abastecimento.km_pendente.all(),
                        'valor_total_mes_anterior': valor_total_mes_anterior,
                        'valor_total_mes_vigente': valor_total_mes_vigente,
                        'diferenca_valores_totais': diferenca_valores_totais,
                        'abastecimentos_mes_vigente': Abastecimento.mes_vigente.all()})
        return context