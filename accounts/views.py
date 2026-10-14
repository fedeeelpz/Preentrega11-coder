from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import MiFormularioRegistro, PerfilForm
from .models import Perfil
def registrar(request):
    if request.method == 'POST':
        form = MiFormularioRegistro(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'¡Cuenta creada exitosamente para {username}! Ya puedes iniciar sesión.')
            return redirect('login')  # Redirige a la página de login
    else:
        form = MiFormularioRegistro()
    
    return render(request, 'accounts/registro.html', {'form': form})

@login_required
def ver_perfil(request):
    perfil, created = Perfil.objects.get_or_create(user=request.user)
    return render(request, 'accounts/perfil.html', {'perfil': perfil})

@login_required
def editar_perfil(request):
    perfil, created = Perfil.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Tu perfil ha sido actualizado con éxito!')
            return redirect('perfil')
    else:
        form = PerfilForm(instance=perfil)
        
    return render(request, 'accounts/editar_perfil.html', {'form': form})