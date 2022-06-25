from django.db import models
from django.forms import CharField

# Create your models here.

class Personaje(models.Model):
    nombre_personaje = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre_personaje

class Caracteristica(models.Model):
    personaje = models.ForeignKey(Personaje, on_delete=models.CASCADE)
    nombre_caracteristica = models.CharField(max_length=15)
    valor = models.CharField(max_length=2, default=0)
    
    def __str__(self):
        return "La característica %s tiene un valor de %s" % (self.nombre_caracteristica,self.valor)

    def bonificador(self):
        bonificador = {1:-30,2:-20,3:-10,4:-5,5:0,6:5,7:5,8:10,9:10,10:15,11:20,12:20,13:25,14:25,15:30,16:35,17:35,18:40,19:40,20:45}
        return bonificador[self.valor]

class Secundaria(models.Model):
    personaje = models.ForeignKey(Personaje, on_delete=models.CASCADE)
    caracteristica = models.ForeignKey(Caracteristica, on_delete=models.CASCADE)
    nombre_secundaria = models.CharField(max_length=200)
    campo = models.CharField(max_length=200)

    coste = models.CharField(max_length=1,default=2)
    valor = models.CharField(max_length=3,default=-30)

    def calculo(self,caracteristica,nuevoValor):
        suma = caracteristica.bonificador() + nuevoValor
        self.valor = suma

    def __str__(self):
        return "%s: %s" % (self.nombre_secundaria,self.valor)