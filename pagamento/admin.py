from django.contrib import admin
from .models import Pagamento

@admin.register(Pagamento)
class PagamentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'compra', 'metodo', 'data_pagamento', 'status')
    list_filter = ('metodo', 'status', 'data_pagamento')
    search_fields = ('compra__id', 'metodo')
