from django.http import HttpRequest
from django.shortcuts import render
from django.shortcuts import render

from formulario.forms import Formularioformulario
from formulario.models import Persona

# Create your views here.

class FormularioformularioPersonaView(HttpRequest):

    def index(request):
        persona = Formularioformulario()
        return render(request, "PersonaFormulario.html", {"form": persona})

    def procesar_formulario(request):
        persona = Formularioformulario(request.POST)
        if persona.is_valid():
            persona.save()
            persona = Formularioformulario()

        return render(request, "PersonaFormulario.html", {"form":persona, "mensaje":'OK'})

    def listar_persona(request):
        personas = Persona.objects.all()
        return render(request,"ListaPersonas.html",{"personas":personas})
