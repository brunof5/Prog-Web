from django.urls import path
from .views import (
    ProdutoListView,
    ProdutoCreateView,
    ProdutoUpdateView,
    ProdutoDeleteView,
)

urlpatterns = [
    path('', ProdutoListView.as_view(), name='lista_produtos'),
    path('novo/', ProdutoCreateView.as_view(), name='novo_produto'),
    path('<int:pk>/editar/', ProdutoUpdateView.as_view(), name='editar_produto'),
    path('<int:pk>/excluir/', ProdutoDeleteView.as_view(), name='excluir_produto'),
]
