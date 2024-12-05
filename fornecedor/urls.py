# fornecedor/urls.py
from django.urls import path
from .views import (
    FornecedorListView,
    FornecedorCreateView,
    FornecedorUpdateView,
    FornecedorDeleteView,
)

urlpatterns = [
    path('', FornecedorListView.as_view(), name='lista_fornecedores'),
    path('novo/', FornecedorCreateView.as_view(), name='novo_fornecedor'),
    path('<int:pk>/editar/', FornecedorUpdateView.as_view(), name='editar_fornecedor'),
    path('<int:pk>/excluir/', FornecedorDeleteView.as_view(), name='excluir_fornecedor'),
]
