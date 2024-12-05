from django.contrib import admin
from .models import Compra

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'data', 'valor_total', 'status')
    list_filter = ('status', 'data')
    search_fields = ('cliente__nome',)
