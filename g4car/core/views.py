from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from core.models import Cliente, Veiculo
from core.forms import FormCliente, FormVeiculo

def home(request):
    return render(request, 'core/index.html')


class Registrar(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'


@login_required
def cadastro_cliente(request):
    form = FormCliente(request.POST or None, request.FILES or None)
    contexto = {'form': form, 'acao': 'Cadastro do cliente', 'titulo': 'Cadastrar cliente'}
    if form.is_valid():
        form.save()
        return redirect('url_listagem_clientes')
    else:
        return render(request, 'core/cadastro_cliente.html', contexto)


@login_required
def listagem_clientes(request):
    clientes = Cliente.objects.all()
    contexto = {'clientes': clientes}
    return render(request, 'core/listagem_clientes.html', contexto)


@login_required
def cadastro_veiculo(request):
    form = FormVeiculo(request.POST or None, request.FILES or None)
    contexto = {'form': form, 'acao': 'Atualizar o cadastro de veiculo', 'titulo': 'Atualizar cadastro'}
    if form.is_valid():
        form.save()
        return redirect('url_listagem_veiculos')
    else:
        return render(request, 'core/cadastro_veiculo.html', contexto)

@login_required
def listagem_veiculos(request):
    veiculos = Veiculo.objects.all()
    contexto = {'veiculos': veiculos}
    return render(request, 'core/listagem_veiculos.html', contexto)

@login_required
def atualiza_cliente(request, id):
    cliente_selecionado = Cliente.objects.get(id=id)
    form = FormCliente(request.POST or None, request.FILES or None, instance=cliente_selecionado)
    contexto = {'form': form, 'acao': 'Atualizar o cadastro do cliente', 'titulo': 'Atualizar cadastro'}
    if form.is_valid():
        form.save()
        return redirect('url_listagem_clientes')
    else:
        return render(request, 'core/cadastro_cliente.html', contexto)

@login_required
def atualiza_veiculo(request, id):
    veiculo_selecionado = Veiculo.objects.get(id=id)
    form = FormVeiculo(request.POST or None, request.FILES or None, instance=veiculo_selecionado)
    contexto = {'form': form, 'acao': 'Atualizar o cadastro de veiculo', 'titulo': 'Atualizar cadastro'}
    if form.is_valid():
        form.save()
        return redirect('url_listagem_veiculos')
    else:
        return render(request, 'core/cadastro_veiculo.html', contexto)

@login_required
def exclui_cliente(request, id):
    try:
        cliente_selecionado = Cliente.objects.get(id=id)
        if request.POST:
            cliente_selecionado.delete()
            return redirect('url_listagem_clientes')
        else:
            return render(request, 'core/confirma_exclusao.html', {'acao': cliente_selecionado.nome, 'redirect': '/listagem_clientes/'})
    except:
        redirect('url_listagem_clientes')

@login_required
def exclui_veiculo(request, id):
    try:
        veiculo_selecionado = Veiculo.objects.get(id=id)
        if request.POST:
            veiculo_selecionado.delete()
            return redirect('url_listagem_veiculos')
        else:
            return render(request, 'core/confirma_exclusao.html', {'acao': veiculo_selecionado.modelo, 'redirect': '/listagem_veiculos/'})
    except:
        return redirect('url_listagem_veiculos')