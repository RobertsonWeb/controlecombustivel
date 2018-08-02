from datetime import datetime
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Abastecimento


class AbastecimentoCreateView(CreateView):
	model = Abastecimento
	fields = ['data', 'posto', 'tipo_combustivel', 'litros', 'valor']
	success_url = reverse_lazy('painel')

	def get_initial(self):
		return {'data': datetime.now().date()}


class AbastecimentoListView(ListView):
	model = Abastecimento


class AbastecimentoUpdateView(UpdateView):
	model = Abastecimento
	fields = ['data', 'posto', 'tipo_combustivel', 'litros', 'valor']
	success_url = reverse_lazy('abastecimento_list')


class AbastecimentoRegistroKmPercorridaUpdateView(UpdateView):
	model = Abastecimento
	fields = ['km_percorridos']
	success_url = reverse_lazy('painel')


class AbastecimentoDeleteView(DeleteView):
	model = Abastecimento
	success_url = reverse_lazy('abastecimento_list')