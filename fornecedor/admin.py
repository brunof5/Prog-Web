from django.contrib import admin
from produtos.models import Produto
from .models import Fornecedor

class ProdutoInline(admin.StackedInline):
    model = Produto
    extra = 1

@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email')
    inlines = [ProdutoInline]
