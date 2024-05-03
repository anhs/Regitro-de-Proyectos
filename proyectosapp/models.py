from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Proyectos(models.Model):
    creacion = models.DateTimeField(auto_now_add=True)
    titulo=models.TextField()
    fecha_de_entrega= models.DateTimeField()
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

class Insidencias(models.Model):
    fe_creacion = models.DateTimeField(auto_now_add=True)
    nombre=models.TextField()
    direccion=models.CharField(max_length=100, blank=True, default='')
    telefono=models.CharField(max_length=10, blank=True, default='')
    id_proyecto=models.IntegerField()
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    #titulo = models.CharField(max_length=100, blank=True, default='')
    #insidencias=models.IntegerField(default=0)
    #insidencias = models.TextField()


    class Meta:
        ordering = ['creacion']
        ordering = ['fe_creacion']
