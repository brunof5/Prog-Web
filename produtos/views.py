from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Produto

class ProdutoListView(ListView):
    model = Produto
    template_name = 'produtos/lista.html'
    context_object_name = 'produtos'

class ProdutoCreateView(CreateView):
    model = Produto
    template_name = 'produtos/formulario.html'
    fields = ['fornecedor', 'nome', 'valor', 'descricao', 'estoque', 'disponivel']
    success_url = reverse_lazy('lista_produtos')

class ProdutoUpdateView(UpdateView):
    model = Produto
    template_name = 'produtos/formulario.html'
    fields = ['fornecedor', 'nome', 'valor', 'descricao', 'estoque', 'disponivel']
    success_url = reverse_lazy('lista_produtos')

class ProdutoDeleteView(DeleteView):
    model = Produto
    template_name = 'produtos/confirmar_exclusao.html'
    success_url = reverse_lazy('lista_produtos')
