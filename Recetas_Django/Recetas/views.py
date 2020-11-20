from django.shortcuts import render

def home(request):
    return render(request,'Recetas/index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, passwoord = password)
        if user:
            login(request, user)
            return redirect ('administracion')
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
    return render(request,'Recetas/formulario.html')

def administracion(request):
    return render(request,'Recetas/Administracion.html')