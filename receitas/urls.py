from django.urls import path

from . import views

# Add funcionalidade de busca das receitas .... o nome= é como se fosse um apelido (alias) para a rota
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:receita_id>', views.receita, name='receita'),
    path('buscar', views.buscar, name='buscar')
]

