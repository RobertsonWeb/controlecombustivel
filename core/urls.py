from django.urls import path
from .views import PainelView, EstatisticaView

urlpatterns = [
	path('', PainelView.as_view(), name='painel'),
	path('estatistica', EstatisticaView.as_view(), name='estatistica')
]
