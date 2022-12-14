from django.contrib import admin

# Register your models here.

from .models import Persona

# Añadimos el modelo para que este sea ejecutado por el Administrador en forma del 
# Proyecto de la aplicacion, mediante el modelo. 
admin.site.register(Persona)
