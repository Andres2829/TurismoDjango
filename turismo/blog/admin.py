from django.contrib import admin
from .models import Post
# Añadimos el modelo para que este sea ejecutado por el Administrador en forma del 
# Proyecto de la aplicacion, mediante el modelo. 
admin.site.register(Post)