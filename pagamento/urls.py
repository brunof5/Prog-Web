from django.urls import path
from .views import (
    PagamentoListView,
    PagamentoCreateView,
    PagamentoUpdateView,
    PagamentoDeleteView,
)

urlpatterns = [
    path('', PagamentoListView.as_view(), name='lista_pagamentos'),
    path('novo/', PagamentoCreateView.as_view(), name='novo_pagamento'),
    path('<int:pk>/editar/', PagamentoUpdateView.as_view(), name='editar_pagamento'),
    path('<int:pk>/excluir/', PagamentoDeleteView.as_view(), name='excluir_pagamento'),
]
