from asyncio import Task
from rest_framework import serializers
from .models import Personaje

class PersonajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personaje
        fields = ('id', 'nombre_personaje')