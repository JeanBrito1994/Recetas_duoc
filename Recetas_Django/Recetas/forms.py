from django import forms
from django.forms import ModelForm, ClearableFileInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Recetas.models import Recetas

class registro(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']

        widgets = {
                'first_name' :forms.TextInput(attrs={'placeholder': 'Juan Esteban'}),
                'username' :forms.TextInput(attrs={'placeholder': 'jpbrito@gmail.com'})
        }

class Buscarid(UserCreationForm):

    class Meta:
        model = User
        fields = ['username']


class modificar(ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

class CustomClearableFileInput(ClearableFileInput):
    template_with_clear = '<br>  <label for="%(clear_checkbox_id)s">%(clear_checkbox_label)s</label> %(clear)s'


class ingresar(ModelForm):
    class Meta:
        model = Recetas
        fields = ['codigo','nombre_receta','instrucciones','ingredientes','imagen']
        widgets = {
            'imagen': CustomClearableFileInput
        }