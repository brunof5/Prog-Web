from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Compra

class CompraListView(ListView):
    model = Compra
    template_name = 'compras/lista.html'
    context_object_name = 'compras'

class CompraCreateView(CreateView):
    model = Compra
    template_name = 'compras/formulario.html'
    fields = ['cliente', 'valor_total', 'status']
    success_url = reverse_lazy('lista_compras')

class CompraUpdateView(UpdateView):
    model = Compra
    template_name = 'compras/formulario.html'
    fields = ['cliente', 'valor_total', 'status']
    success_url = reverse_lazy('lista_compras')

class CompraDeleteView(DeleteView):
    model = Compra
    template_name = 'compras/confirmar_exclusao.html'
    success_url = reverse_lazy('lista_compras')
