from django.urls import path
from .views import AbastecimentoCreateView, AbastecimentoListView
from .views import AbastecimentoUpdateView,AbastecimentoRegistroKmPercorridaUpdateView
from .views import AbastecimentoDeleteView

urlpatterns = [
	path('add', AbastecimentoCreateView.as_view(), name='abastecimento_add'),
	path('list', AbastecimentoListView.as_view(), name='abastecimento_list'),
	path('<int:pk>/', AbastecimentoUpdateView.as_view(), name='abastecimento_change'),
	path('km-percorrida/<int:pk>/', AbastecimentoRegistroKmPercorridaUpdateView.as_view(), name='abastecimento_km_percorrida'),
	path('<int:pk>/delete/', AbastecimentoDeleteView.as_view(), name='abastecimento_delete')
]