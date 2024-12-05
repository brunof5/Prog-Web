from django.contrib import admin
from .models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'fornecedor', 'valor', 'estoque', 'disponivel')
    list_filter = ('fornecedor', 'disponivel')
    search_fields = ('nome', 'descricao')
