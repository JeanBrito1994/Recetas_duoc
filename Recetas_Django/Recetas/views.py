from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from Recetas.models import usuarios
from Recetas.forms import UserCreationForm, registro
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request,'Recetas/index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password = password)
        if user:
            login(request, user)
            return redirect ('home')
        else:
            return render(request,'Recetas/Login.html', {'error':'Credenciales invalidas'})
    return render(request,'Recetas/Login.html')

def recetas(request):
    return render(request,'Recetas/Recetas.html')

def entradas(request):
    return render(request,'Recetas/Entradas.html')

def fondo(request):
    return render(request,'Recetas/Fondo.html')

def postres(request):
    return render(request,'Recetas/Postres.html')

def acerca(request):
    return render(request,'Recetas/Acerca.html')

def formulario(request):
    data = {
        'form': registro()
    }
    if request.method == 'POST':
        formulario = registro(request.POST)
        if formulario.is_valid():
            formulario.save()
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect ('home')
        else:
            return render(request,'Recetas/formulario.html', {'error':'No se puedo ingresar el usuario'})

    return render(request,'Recetas/formulario.html', data)

@login_required
def administracion(request):
    return render(request,'Recetas/Administracion.html')

