from django.contrib import admin
from .models import Pessoa

# Register your models here.

class ListandoPessoa(admin.ModelAdmin):  # Editando as informações que serão mostradas no gerenciador admin do site
    list_display = ('id', 'nome', 'email')  # Selecionando os campos de interesse p/ serem visualizados
    list_display_links = ('id', 'nome') # Selecionando os campos de interesse p/ se comportarem como link
    search_fields = ('nome',)  # Add um campo busca na pagina adimin para pesquisar dados cadastrados
    list_per_page = 2  # Add no site admin um metodo de visualização por páginas, assim o inteiro informado será a quantidade de itens por página

admin.site.register(Pessoa, ListandoPessoa)