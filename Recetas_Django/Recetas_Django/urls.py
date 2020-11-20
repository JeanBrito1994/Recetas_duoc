
from django.contrib import admin
from django.urls import path
from Recetas import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('login/', views.login_view,name='login'),
    path('recetas/', views.recetas,name='recetas'),
    path('entradas/', views.entradas,name='entradas'),
    path('fondo/', views.fondo,name='fondo'),
    path('postres/', views.postres,name='postres'),
    path('acerca/', views.acerca,name='acerca'),
    path('formulario/', views.formulario,name='formulario'),
    path('administracion/', views.administracion,name='administracion'),

]
