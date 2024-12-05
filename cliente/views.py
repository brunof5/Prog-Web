from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Cliente
from django.http import HttpResponse
from django.template import loader

def principal(request):
    template = loader.get_template('principal.html')
    return HttpResponse(template.render())

@login_required
def perfil_cliente(request):
    cliente = Cliente.objects.get(user=request.user)
    return render(request, 'cliente/perfil.html', {'cliente': cliente})


