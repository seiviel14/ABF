from audioop import reverse
from urllib import request
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Caracteristica, Personaje, Secundaria
from .forms import CrearPersonaje
from .static.fichapersonaje.tablas.tablas import campos_secundarias, secundarias_caracteristicas

'''secundarias_caracteristicas = {
    "agi":["Acrobacias", "Atletismo", "Montar", "Nadar","Trepar", "Sigilo", "Baile"],
    "con":[],
    "des":["Pilotar", "Cerrajería", "Disfraz", "Ocultarse", "Robo", "Trampería", "T. Manos", "Caligrafía ritual", "Orfebrería", "Confección"],
    "fue":["Saltar", "P. Fuerza", "Forja", "Runas"],
    "int":["Persuasión", "Comercio", "Callejeo", "Etiqueta", "Animales", "Ciencia", "Ley", "Herbolaria", "Historia", "Tactica", "Medicina", "Memorizar", "Navegación", "Ocultismo", "Tasación", "Venenos", "Alquimia"],
    "per":["Advertir", "Buscar", "Rastrear"],
    "pod":["Estilo", "Liderazgo", "V. Mágica", "Arte", "Animismo", "Música", "Conf. marionetas"],
    "vol":["Intimidar", "Frialdad", "Res. Dolor"]
}
campos_secundarias = {
    "Atleticas":["Acrobacias", "Atletismo", "Montar", "Nadar", "Trepar", "Saltar", "Pilotar"],
    "Sociales":["Estilo", "Intimidar", "Liderazgo", "Persuasión", "Comercio", "Callejeo", "Etiqueta"],
    "Percepcion":["Advertir", "Buscar", "Rastrear"],
    "Intelectuales":["Animales", "Ciencia", "Ley", "Herbolaria", "Historia", "Tactica", "Medicina", "Memorizar", "Navegación", "Ocultismo", "Tasación", "V. Mágica"],
    "Vigor":["Frialdad", "P. Fuerza", "Res. Dolor"],
    "Subterfugio":["Cerrajería", "Disfraz", "Ocultarse", "Robo", "Sigilo", "Trampería", "Venenos"],
    "Creativas":["Arte", "Baile", "Forja", "Runas", "Alquimia", "Animismo", "Música", "T. Manos", "Caligrafía ritual", "Orfebrería", "Confección", "Conf. marionetas"],
}'''

# Create your views here.
class IndexView(generic.ListView):
    template_name = "fichapersonaje/index.html"
    context_object_name = "personajes"

    def get_queryset(self):
        return Personaje.objects.all()

class PersonajeView(generic.DetailView):
    template_name = "fichapersonaje/detail.html"
    model = Personaje
    
    def get_queryset(self):
        return Personaje.objects.all()

class CambiarDatosView(generic.DetailView):
    template_name = "fichapersonaje/cambiardatos.html"
    model = Personaje

    def get_queryset(self):
        return Personaje.objects.all()

#Vista que utilizaremos para crear un personaje mediante una modelForm
def crearPersonaje(request):
    if request.method == 'POST':
        form = CrearPersonaje(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('fichapersonaje:index'))
    else:
            form = CrearPersonaje()
    return render(request, 'fichapersonaje/crearpersonaje.html', { 'form': form})

#Vista que utilizaremos para cambiar datos de un personaje
def cambioDatos(request, personaje_id):
    personaje = get_object_or_404(Personaje, pk=personaje_id)
    personaje.nombre_personaje = request.POST.get('nombre') #Es el nombre del formulario que se envía en el template de detail
    for nombre_caracteristica in secundarias_caracteristicas:
        caracteristica = get_object_or_404(Caracteristica, personaje = personaje, nombre_caracteristica = nombre_caracteristica)
        caracteristica.valor = request.POST.get(nombre_caracteristica)
        caracteristica.save()

        for nombre_secundaria in secundarias_caracteristicas[nombre_caracteristica]:
            secundaria = get_object_or_404(Secundaria, personaje = personaje, caracteristica = caracteristica, nombre_secundaria = nombre_secundaria)
            secundaria.valor = request.POST.get(nombre_secundaria)
            secundaria.save()

    personaje.save()
    return HttpResponseRedirect(reverse('fichapersonaje:detail', args=(personaje.id,)))
        
    

#Vista que utilizaremos para eliminar los personajes
def eliminarPersonaje(request, personaje_id):
    Personaje.objects.get(pk=personaje_id).delete()
    return HttpResponseRedirect(reverse('fichapersonaje:index'))

'''def crearDetalles(request, personaje_id):
    personaje = get_object_or_404(Personaje, pk=personaje_id)
    if not Caracteristica.objects.filter(personaje=personaje):
        for nombre_caracteristica in secundarias_caracteristicas:
            Caracteristica.objects.create(personaje=personaje,nombre_caracteristica=nombre_caracteristica )
            caracteristica = Caracteristica.objects.get(personaje=personaje,nombre_caracteristica=nombre_caracteristica )

            for secundaria in secundarias_caracteristicas[nombre_caracteristica]:
                campo_secundaria = [campo for campo, secundarias in campos_secundarias.items() for secundaria_nombre in secundarias if secundaria_nombre == secundaria]
                Secundaria.objects.create(personaje=personaje, caracteristica=caracteristica,nombre_secundaria=secundaria, campo=campo_secundaria[0])
                
        return HttpResponseRedirect(reverse('fichapersonaje:detail', args=(personaje.id,)))
    else:
        return HttpResponseRedirect(reverse('fichapersonaje:detail', args=(personaje.id,)))'''

def crearDetalles(request, personaje_id):
    personaje = get_object_or_404(Personaje, pk=personaje_id)
    if not Caracteristica.objects.filter(personaje=personaje):
        for nombre_caracteristica in secundarias_caracteristicas:
            Caracteristica.objects.create(personaje=personaje,nombre_caracteristica=nombre_caracteristica )
            '''caracteristica = Caracteristica.objects.get(personaje=personaje,nombre_caracteristica=nombre_caracteristica )

            for secundaria in secundarias_caracteristicas[nombre_caracteristica]:
                campo_secundaria = [campo for campo, secundarias in campos_secundarias.items() for secundaria_nombre in secundarias if secundaria_nombre == secundaria]
                Secundaria.objects.create(personaje=personaje, caracteristica=caracteristica,nombre_secundaria=secundaria, campo=campo_secundaria[0])'''

        for campo in campos_secundarias:
            for secundaria in campos_secundarias[campo]:
                caracteristica_secundaria = [caracteristica for caracteristica, secundarias in secundarias_caracteristicas.items() for secundaria_nombre in secundarias if secundaria_nombre == secundaria]
                caracteristica = get_object_or_404(Caracteristica, personaje = personaje, nombre_caracteristica = caracteristica_secundaria[0])
                Secundaria.objects.create(personaje = personaje, caracteristica = caracteristica, nombre_secundaria = secundaria, campo = campo)

        return HttpResponseRedirect(reverse('fichapersonaje:detail', args=(personaje.id,)))
    else:
        return HttpResponseRedirect(reverse('fichapersonaje:detail', args=(personaje.id,)))