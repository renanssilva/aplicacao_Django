from django.contrib import admin
from .models import Receita


# Register your models here.

# Aqui registramos todos nossos modelos e dinamica que ira manipular as informações


class ListandoReceitas(admin.ModelAdmin):  # Editando as informações que serão mostradas no gerenciador admin do site
    list_display = ('id', 'nome_receita', 'categoria', 'tempo_preparo', 'publicada')  # Selecionando os campos de interesse p/ serem visualizados
    list_display_links = ('nome_receita',) # Selecionando os campos de interesse p/ se comportarem como link
    search_fields = ('nome_receita',)  # Add um campo busca na pagina adimin para pesquisar dados cadastrados
    list_filter = ('categoria',)  # Add no site admin um filtro de busca com todas as opções registradas  no argumento passado
    list_editable = ('publicada',)  # CRiar uma lista com os campos que podem ser editados
    list_per_page = 10  # Add no site admin um metodo de visualização por páginas, assim o inteiro informado será a quantidade de itens por página


admin.site.register(Receita, ListandoReceitas)


