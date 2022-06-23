from django.db import models
from django.forms import CharField, ModelForm

from .models import Personaje, Caracteristicas

class CrearPersonaje(ModelForm):
    class Meta:
        model = Personaje
        fields = ['nombre_personaje',]