from django.shortcuts import render, redirect
from django.contrib.auth.models import User  # Vamos usar o USER para verificar se já existe um usuario(modelo) cadastrado
from django.contrib import auth  # auth -> user authentication(autenticação de usuario)


def cadastro(request):
    if request.method == 'POST':

        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']

        if not nome.strip():
            print('O campo nome não pode ficar em branco')
            return redirect('cadastro')

        if not email.strip():
            print('O campo email não pode ficar em branco')
            return redirect('cadastro')

        if senha != senha2:
            print('As senhas não são iguais')
            return redirect('cadastro')

        if User.objects.filter(email=email).exists():
            print('Usuario já cadastrado')
            return redirect('cadastro')

        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        print('Usuario cadastrado com sucesso')
        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']

        if email == "" or senha == "":
            print('Os compos email e senha não podem ficar em branco')
            return redirect('login')

        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            print(user)
            if user is not None:
                auth.login(request, user)
                print('Login realizado com sucesso')
                return redirect('dashboard')
    return render(request, 'usuarios/login.html')


def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'usuarios/dashboard.html')
    else:
        return redirect('index')


def logout(request):
    auth.logout(request)
    return redirect('index')