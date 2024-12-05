from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Pagamento

class PagamentoListView(ListView):
    model = Pagamento
    template_name = 'pagamento/lista.html'
    context_object_name = 'pagamentos'

class PagamentoCreateView(CreateView):
    model = Pagamento
    template_name = 'pagamento/formulario.html'
    fields = ['compra', 'metodo', 'data_pagamento', 'status']
    success_url = reverse_lazy('lista_pagamentos')

class PagamentoUpdateView(UpdateView):
    model = Pagamento
    template_name = 'pagamento/formulario.html'
    fields = ['compra', 'metodo', 'data_pagamento', 'status']
    success_url = reverse_lazy('lista_pagamentos')

class PagamentoDeleteView(DeleteView):
    model = Pagamento
    template_name = 'pagamento/confirmar_exclusao.html'
    success_url = reverse_lazy('lista_pagamentos')
