from django.urls import path
from .views import PainelView

urlpatterns = [
	path('', PainelView.as_view(), name='painel')
]
