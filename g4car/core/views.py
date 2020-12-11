from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from core.models import Cliente, Veiculo, Parametro, \
                        Movimento, Mensalista
from core.forms import FormCliente, FormVeiculo, \
    FormParametro, FormMovimento, FormMensalista
# Create your views here.


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
    if request.POST:
        if request.POST['nome']:
            clientes = Cliente.objects.filter(nome=request.POST['nome'])
        else:
            clientes = Cliente.objects.all()
    else:
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
        contexto = {'acao': cliente_selecionado.nome, 'redirect': '/listagem_clientes/'}
        if request.POST:
            cliente_selecionado.delete()
            return redirect('url_listagem_clientes')
        else:
            return render(request, 'core/confirma_exclusao.html', contexto)
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


@login_required
def cadastro_parametro(request):
    form = FormParametro(request.POST or None)
    contexto = {'form': form, 'acao': 'Cadastro de Parametro', 'titulo': 'Cadastro de Parametro'}
    if form.is_valid():
        form.save()
        return redirect('url_listagem_parametros')
    else:
        return render(request, 'core/cadastro_parametro.html', contexto)


@login_required
def listagem_parametros(request):
    dados = Parametro.objects.all()
    contexto = {'parametros': dados}
    return render(request, 'core/listagem_parametros.html', contexto)


@login_required
def cadastro_mensalista(request):
    form = FormMensalista(request.POST or None)
    contexto = {'form': form, 'acao': 'Cadastro de mensalista', 'titulo': 'Cadastro de mensalista'}
    if form.is_valid():
        form.save()
        return redirect('url_listagem_mensalistas')
    else:
        return render(request, 'core/cadastro_mensalista.html', contexto)


@login_required
def listagem_mensalistas(request):
    dados = Mensalista.objects.all()
    contexto = {'mensalistas': dados}
    return render(request, 'core/listagem_mensalistas.html', contexto)


@login_required
def atualiza_parametro(request, id):
    try:
        obj = Parametro.objects.get(id=id)
        form = FormParametro(request.POST or None, instance=obj)
        contexto = {'form': form, 'acao': 'Atualizacao de parametro'}
        if form.is_valid():
            form.save()
            return redirect('url_listagem_parametros')
        else:
            return render(request, 'core/cadastro_mensalista.html', contexto)
    except:
        return redirect('url_listagem_parametros')


@login_required
def exclui_parametro(request, id):
    obj = Parametro.objects.get(id=id)
    contexto = {'acao': obj.descricao, 'redirect': '/listagem_parametros/'}
    if request.method == 'POST':
        obj.delete()
        return redirect('url_listagem_parametros')
    else:
        return render(request, 'core/confirma_exclusao.html', contexto)
