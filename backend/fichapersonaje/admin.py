from django.contrib import admin
from .models import Personaje

# Register your models here.
class PersonajeAdmin(admin.ModelAdmin):
    list = ('nombre_personaje')

admin.site.register(Personaje, PersonajeAdmin)