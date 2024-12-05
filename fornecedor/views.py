from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Fornecedor

class FornecedorListView(ListView):
    model = Fornecedor
    template_name = 'fornecedor/lista.html'
    context_object_name = 'fornecedores'

class FornecedorCreateView(CreateView):
    model = Fornecedor
    template_name = 'fornecedor/formulario.html'
    fields = ['nome', 'endereco', 'email']
    success_url = reverse_lazy('lista_fornecedores')

class FornecedorUpdateView(UpdateView):
    model = Fornecedor
    template_name = 'fornecedor/formulario.html'
    fields = ['nome', 'endereco', 'email']
    success_url = reverse_lazy('lista_fornecedores')

class FornecedorDeleteView(DeleteView):
    model = Fornecedor
    template_name = 'fornecedor/confirmar_exclusao.html'
    success_url = reverse_lazy('lista_fornecedores')
