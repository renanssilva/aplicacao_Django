from receitas.models import Receita
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404

def busca(request):
    # PEgando todas as receitas publicadas e ordenadas
    lista_receitas = Receita.objects.order_by('-date_receita').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        # if nome_a_buscar:
        lista_receitas = lista_receitas.filter(nome_receita__icontains=nome_a_buscar)

    dados = {
        'receitas': lista_receitas
    }

    return render(request, 'receitas/buscar.html', dados)