from django.db import models

from django.db import models
from django.db.models.fields import CharField, DateField, URLField
from django.db.models.fields.files import ImageField
from datetime import date

# añadimos las etiquetas que seran entregadas a la vista del administrador y de los usuarios
# siendo estos los campos a crear segun los requerimientos del programa como
# lo son los municipios con un titulo, descripcion, imagen etc...
class Project(models.Model):
    title = CharField(max_length=100)
    description = CharField(max_length=250)
    image = ImageField(upload_to="portfolio/images")
    url = URLField(blank=True)
    date = DateField(default=date.today)

    def __str__(self) -> str:
        return self.title
