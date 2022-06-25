from django.db import models
from django.forms import CharField, ModelForm

from .models import Personaje

class CrearPersonaje(ModelForm):
    class Meta:
        model = Personaje
        fields = ['nombre_personaje',]
