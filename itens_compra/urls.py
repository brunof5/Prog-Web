from django.urls import path
from .views import (
    ItensCompraListView,
    ItensCompraCreateView,
    ItensCompraUpdateView,
    ItensCompraDeleteView,
)

urlpatterns = [
    path('', ItensCompraListView.as_view(), name='lista_itens_compra'),
    path('novo/', ItensCompraCreateView.as_view(), name='novo_item_compra'),
    path('<int:pk>/editar/', ItensCompraUpdateView.as_view(), name='editar_item_compra'),
    path('<int:pk>/excluir/', ItensCompraDeleteView.as_view(), name='excluir_item_compra'),
]
