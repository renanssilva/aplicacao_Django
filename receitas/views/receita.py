from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth.models import User  # Vamos usar o USER para verificar se já existe um usuario(modelo) cadastrado
from receitas.models import Receita
from django.contrib import auth, messages  # auth -> user authentication(autenticação de usuario)


# Create your views here.

# Responsavel por renderizar as paginas

def index(request):

    # Receita.objects.all() --> Estamos pegando todos os objetos que são nossas receitas
    # receitas = Receita.objects.all()  # instalar e configurar o 'pylint-django' para verificação de código

    # Agora temos dois estados das receitas(publicada e não publicada) assim devemos mudar o Receita.objects.all()
    # receitas = Receita.objects.filter(publicada=True)  # em vez de all() passamos um filtro filter(campo=True)

    # Agora vamos adicionar um filtro de ordenação antes do filtro de receita publicada. Passando o método
    # order_by('-date_receita') para ordenar de acordo com a data. O sinal '-' é para ordernarmos das mais novas 1º
    receitas = Receita.objects.order_by('-date_receita').filter(publicada=True)  # coloque order_by('-date_receita')

    dados = {
        'receitas': receitas
    }

    # renderizando(render)(requisisão(request),template(o nome da pagina do site), contexto(Um dicionario com chave e valor))
    return render(request, 'receitas/index.html', dados)


def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)

    receita_a_exibir = {
        'receita': receita
    }

    return render(request, 'receitas/receita.html', receita_a_exibir)


def cria_receita(request):
    if request.method == 'POST':
        nome_receita = request.POST['nome_receita']
        ingredientes = request.POST['ingredientes']
        modo_preparo = request.POST['modo_preparo']
        tempo_preparo = request.POST['tempo_preparo']
        rendimento = request.POST['rendimento']
        categoria = request.POST['categoria']
        foto_receita = request.FILES['foto_receita']

        user = get_object_or_404(User, pk=request.user.id)

        receita = Receita.objects.create(pessoa=user, nome_receita=nome_receita, ingredientes=ingredientes,
                                        modo_preparo=modo_preparo, tempo_preparo=tempo_preparo, rendimento=rendimento,
                                         categoria=categoria, foto_receita=foto_receita)

        receita.save()
        return redirect('dashboard')
    else:
        return render(request, 'receitas/cria_receita.html')


def deleta_receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    receita.delete()
    return redirect('dashboard')


def edita_receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    receita_a_editar = {'receita': receita}
    return render(request, 'receitas/edita_receita.html', receita_a_editar)


def atualiza_receita(request):
    if request.method == 'POST':
        receita_id = request.POST['receita_id']
        r = Receita.objects.get(pk=receita_id)
        r.nome_receita = request.POST['nome_receita']
        r.ingredientes = request.POST['ingredientes']
        r.modo_preparo = request.POST['modo_preparo']
        r.tempo_preparo = request.POST['tempo_preparo']
        r.rendimento = request.POST['rendimento']
        r.categoria = request.POST['categoria']
        if 'foto_receita' in request.FILES:
            r.foto_receita = request.FILES['foto_receita']

        r.save()
        return redirect('dashboard')
