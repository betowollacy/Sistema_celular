from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
from django.shortcuts import redirect #redireciador de paginas
from hashlib import sha256 #codificar a senha

def login(request):
    status = request.GET.get('status')
    return render(request,'Login.html', {'status': status})


def cadastro(request):
    status = request.GET.get('status')
    return render(request,'Cadastro.html', {'status': status})


def valida_cadastro(request):
    nome =  request.POST.get('nome')
    email =  request.POST.get('email')
    senha =  request.POST.get('senha')

    usuario = Usuario.objects.filter(email = email)

    if len(nome.strip()) == 0 or len(email.strip()) == 0:
        return redirect('/auth/cadastro/?status=1')

    if len(senha) < 8:
        return redirect('/auth/cadastro/?status=2')  

    if len(usuario) > 0:
        return redirect('/auth/cadastro/?status=3')

    try:
        senha = sha256(senha.encode()).hexdigest()
        usuario = Usuario(nome = nome, senha = senha, email = email)
        usuario.save()

        return redirect('/auth/cadastro/?status=0')  

    except:
        return redirect('/auth/cadastro/?status=4')     


def valida_login(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    senha = sha256(senha.encode()).hexdigest()

    usuario = Usuario.objects.filter(email = email).filter(senha = senha)

    if len(usuario) == 0:
        return redirect('/auth/login/?status=1')
        
    elif len(usuario) > 0:
        request.session['usuario'] = usuario[0].id
        return redirect('/aparelho/home/')    

def sair(request):
    request.session.flush() 
    return redirect('/auth/login/') 