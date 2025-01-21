from django.contrib import admin
from .models import ItensCompra

@admin.register(ItensCompra)
class ItensCompraAdmin(admin.ModelAdmin):
    list_display = ('id', 'compra', 'produto', 'quantidade', 'preco_unitario')
    readonly_fields = ['preco_unitario']
