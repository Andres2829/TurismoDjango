from dataclasses import fields
from django import forms
from formulario.models import Persona

class Formularioformulario(forms.ModelForm):
    class Meta: 
        model = Persona
        fields = ('nombres','apellidos','cedula','telefono','correo','profesion','residencia','destino','habilidades')

