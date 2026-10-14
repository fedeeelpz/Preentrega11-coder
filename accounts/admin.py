from django.contrib import admin

# Register your models here.
from .models import Perfil

# Registramos el modelo en el panel de administración
admin.site.register(Perfil)