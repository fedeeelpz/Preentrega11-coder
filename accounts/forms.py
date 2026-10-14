from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Perfil

class MiFormularioRegistro(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['biografia', 'link_web', 'avatar']