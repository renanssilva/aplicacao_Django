from django.urls import path

from . import views

# Add funcionalidade de busca das receitas .... o nome= é como se fosse um apelido (alias) para a rota
urlpatterns = [
    path('cadastro', views.cadastro, name='cadastro'),
    path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout, name='logout'),
    path('cria/receita', views.cria_receita, name='cria_receita')
]

