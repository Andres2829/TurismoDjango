from django.db import models
from django.db.models.fields import CharField, DateField, URLField
import datetime

# añadimos las etiquetas que seran entregadas a la vista del administrador y de los usuarios
# siendo estos los campos a crear segun los requerimientos del programa como
# lo son los municipios con un titulo, descripcion, imagen etc...
class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="blog/images")
    date = models.DateField(default=datetime.date.today)
    urlmapa= models.TextField()

    def __str__(self) -> str:
        return self.title