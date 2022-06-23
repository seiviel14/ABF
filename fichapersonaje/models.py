from pyexpat import model
from django.db import models
from django.forms import CharField

# Create your models here.

class Personaje(models.Model):
    nombre_personaje = models.CharField(max_length=200)


    def __str__(self):
        return self.nombre_personaje

class Caracteristicas(models.Model):
    personaje = models.ForeignKey(Personaje, on_delete=models.CASCADE)
    nombre_característica = models.CharField(max_length=15)
    caracteristica = models.CharField(max_length=2)
    
    def __str__(self):
        return "Las característica %d tiene un valor de %d",(self.nombre_característica,self.caracteristica)