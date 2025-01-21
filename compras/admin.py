from django.contrib import admin
from .models import Compra
from itens_compra.models import ItensCompra
from pagamento.models import Pagamento

class ItensCompraInline(admin.StackedInline):
    model = ItensCompra
    extra = 1
    readonly_fields = ['preco_unitario']

class PagamentoInline(admin.StackedInline):
    model = Pagamento
    extra = 0

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'data', 'valor_total', 'status')
    list_filter = ('cliente', 'status')
    readonly_fields = ['valor_total']
    inlines = [ItensCompraInline, PagamentoInline]
