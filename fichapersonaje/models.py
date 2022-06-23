from django.db import models
from django.forms import CharField

# Create your models here.

class Personaje(models.Model):
    nombre_personaje = models.CharField(max_length=200)
    caracteristicas = []

    '''def crear_caracteristicas(self):
        caracteristicas = [
        Caracteristicas(personaje = self.pk, nombre_caracteristica = "agi"),
        Caracteristicas(personaje = self.pk, nombre_caracteristica = "con"),
        Caracteristicas(personaje = self.pk, nombre_caracteristica = "des"),
        Caracteristicas(personaje = self.pk, nombre_caracteristica = "fue"),
        Caracteristicas(personaje = self.pk, nombre_caracteristica = "int"),
        Caracteristicas(personaje = self.pk, nombre_caracteristica = "per"),
        Caracteristicas(personaje = self.pk, nombre_caracteristica = "pod"),
        Caracteristicas(personaje = self.pk, nombre_caracteristica = "vol")]'''

    def __str__(self):
        return self.nombre_personaje

class Caracteristicas(models.Model):
    personaje = models.ForeignKey(Personaje, on_delete=models.CASCADE)
    nombre_caracteristica = models.CharField(max_length=15)
    caracteristica = models.CharField(max_length=2)
    
    def __str__(self):
        return "Las característica %d tiene un valor de %d",(self.nombre_característica,self.caracteristica)