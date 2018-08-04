from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from abastecimento.models import Abastecimento


class PainelView(LoginRequiredMixin, TemplateView):
    template_name = 'core/painel.html'

    def get_context_data(self, **kwargs):
        context = super(PainelView, self).get_context_data(**kwargs)
        context.update({'abastecimentos_km_pendente': Abastecimento.km_pendente.all()})
        return context



class EstatisticaView(LoginRequiredMixin, TemplateView):
    template_name = 'core/estatistica.html'

    def get_context_data(self, **kwargs):
        valor_total_mes_anterior = Abastecimento.mes_anterior.all()['valor_total']
        valor_total_mes_vigente = Abastecimento.mes_vigente.all()['valor_total']
        diferenca_valores_totais = valor_total_mes_anterior - valor_total_mes_vigente
        context = super(EstatisticaView, self).get_context_data(**kwargs)
        context.update({'valor_total_mes_anterior': valor_total_mes_anterior,
                        'valor_total_mes_vigente': valor_total_mes_vigente,
                        'diferenca_valores_totais': diferenca_valores_totais,
                        'abastecimentos_mes_vigente': Abastecimento.mes_vigente.all(),
                        'melhor_rendimento_mes': Abastecimento.melhor_rendimento_mes.all()})
        return context