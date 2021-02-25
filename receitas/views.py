from django.shortcuts import render, get_list_or_404, get_object_or_404

from receitas.models import Receita

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
    return render(request, 'index.html', dados)


def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)

    receita_a_exibir = {
        'receita' : receita
    }

    return render(request,'receita.html', receita_a_exibir)


def buscar(request):
    # PEgando todas as receitas publicadas e ordenadas
    lista_receitas = Receita.objects.order_by('-date_receita').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            lista_receitas = lista_receitas.filter(nome_receita__icontains=nome_a_buscar)

    dados = {
        'receitas': lista_receitas
    }

    return render(request, 'buscar.html', dados)
