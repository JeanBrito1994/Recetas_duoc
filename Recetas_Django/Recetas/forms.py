from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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