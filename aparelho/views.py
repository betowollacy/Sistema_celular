from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from usuarios.models import Usuario
from .models import Aparelhos

# Create your views here.
def home(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario'])
        aparelho = Aparelhos.objects.filter(usuario=usuario)
        return render(request, 'home.html', {'aparelho': aparelho} )

    else:
        return redirect('/auth/login/?status=2')   