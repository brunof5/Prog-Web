from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import ItensCompra

class ItensCompraListView(ListView):
    model = ItensCompra
    template_name = 'itens_compra/lista.html'
    context_object_name = 'itens_compra'

class ItensCompraCreateView(CreateView):
    model = ItensCompra
    template_name = 'itens_compra/formulario.html'
    fields = ['compra', 'produto', 'quantidade', 'preco_unitario']
    success_url = reverse_lazy('lista_itens_compra')

class ItensCompraUpdateView(UpdateView):
    model = ItensCompra
    template_name = 'itens_compra/formulario.html'
    fields = ['compra', 'produto', 'quantidade', 'preco_unitario']
    success_url = reverse_lazy('lista_itens_compra')

class ItensCompraDeleteView(DeleteView):
    model = ItensCompra
    template_name = 'itens_compra/confirmar_exclusao.html'
    success_url = reverse_lazy('lista_itens_compra')
