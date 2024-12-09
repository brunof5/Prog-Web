from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import Cliente

def base_cliente(request):
    template = loader.get_template('cliente/base_cliente.html')
    return HttpResponse(template.render())

def perfil_cliente(request, pk):
    cliente = get_object_or_404(Cliente, id=pk)
    template = loader.get_template('cliente/perfil.html')
    context = {'cliente': cliente}
    return HttpResponse(template.render(context, request))

def listar_clientes(request):
    clientes = Cliente.objects.all()
    template = loader.get_template('cliente/listar.html')
    context = {'clientes': clientes}
    return HttpResponse(template.render(context, request))

def criar_cliente(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        endereco = request.POST.get('endereco')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        Cliente.objects.create(
            nome=nome,
            idade=idade,
            endereco=endereco,
            email=email,
            telefone=telefone
        )
        return HttpResponseRedirect(reverse('cliente:listar_clientes'))

    template = loader.get_template('cliente/criar.html')
    return HttpResponse(template.render({}, request))

def atualizar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, id=pk)
    if request.method == 'POST':
        cliente.nome = request.POST.get('nome')
        cliente.idade = request.POST.get('idade')
        cliente.endereco = request.POST.get('endereco')
        cliente.email = request.POST.get('email')
        cliente.telefone = request.POST.get('telefone')
        cliente.save()
        return HttpResponseRedirect(reverse('cliente:listar_clientes'))

    template = loader.get_template('cliente/atualizar.html')
    context = {'cliente': cliente}
    return HttpResponse(template.render(context, request))

def deletar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, id=pk)
    if request.method == 'POST':
        cliente.delete()
        return HttpResponseRedirect(reverse('cliente:listar_clientes'))

    template = loader.get_template('cliente/deletar.html')
    context = {'cliente': cliente}
    return HttpResponse(template.render(context, request))
