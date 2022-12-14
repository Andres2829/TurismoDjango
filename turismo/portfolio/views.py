from django.shortcuts import render
from .models import Project

# Añadimos una funcion que realiza la peticion a las rutas que son las vistas al usuario
# enviada desde el parametro del modelo y del proyecto creado a la vista HTML
def home(request):
    projects = Project.objects.all()
    return render(request, "home.html", {"projects": projects})

def gastronomia(request):
    projects = Project.objects.all()
    return render(request, "gastronomia.html", {"projects": projects})

def etnoturismo (request):
    projects = Project.objects.all()
    return render(request, "etnoturismo.html", {"projects": projects})

def patronales (request):
    projects = Project.objects.all()
    return render(request, "patronales.html", {"projects": projects})