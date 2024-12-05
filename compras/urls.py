from django.urls import path
from .views import (
    CompraListView,
    CompraCreateView,
    CompraUpdateView,
    CompraDeleteView,
)

urlpatterns = [
    path('', CompraListView.as_view(), name='lista_compras'),
    path('nova/', CompraCreateView.as_view(), name='nova_compra'),
    path('<int:pk>/editar/', CompraUpdateView.as_view(), name='editar_compra'),
    path('<int:pk>/excluir/', CompraDeleteView.as_view(), name='excluir_compra'),
]
