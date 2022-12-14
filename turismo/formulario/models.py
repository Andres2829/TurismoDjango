from django.db import models

# Create your models here.
class Persona(models.Model):
    nombres=models.CharField(max_length=150)
    apellidos=models.CharField(max_length=150)
    cedula=models.IntegerField()
    telefono=models.CharField(max_length=150)
    correo=models.CharField(max_length=150)
    profesion=models.CharField(max_length=150)
    residencia=models.CharField(max_length=150)
    destino=models.CharField(max_length=150)
    habilidades=models.CharField(max_length=150)
    estado=models.CharField(max_length=150,default='PENDIENTE')
  