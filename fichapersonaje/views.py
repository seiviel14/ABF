from audioop import reverse
from urllib import request
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Caracteristicas, Personaje
from .forms import CrearPersonaje

caracteristicas = ["agi","con","des","fue","int","per","pod","vol"]

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
def cambiarDatos(request, personaje_id):
    personaje = get_object_or_404(Personaje, pk=personaje_id)
    personaje.nombre_personaje = request.POST.get('nombre') #Es el nombre del formulario que se envía en el template de detail
    for nombre_caracteristica in caracteristicas:
        caracteristica = get_object_or_404(Caracteristicas, personaje = personaje, nombre_caracteristica=nombre_caracteristica)
        caracteristica.valor = request.POST.get(nombre_caracteristica)
        caracteristica.save()
    personaje.save()
    return HttpResponseRedirect(reverse('fichapersonaje:index'))
        
    

#Vista que utilizaremos para eliminar los personajes
def eliminarPersonaje(request, personaje_id):
    Personaje.objects.get(pk=personaje_id).delete()
    return HttpResponseRedirect(reverse('fichapersonaje:index'))

def crearDetalles(request, personaje_id):
    personaje = get_object_or_404(Personaje, pk=personaje_id)
    if not Caracteristicas.objects.filter(personaje=personaje):
        for caracteristica in caracteristicas:
            Caracteristicas.objects.create(personaje=personaje,nombre_caracteristica=caracteristica)
        return HttpResponseRedirect(reverse('fichapersonaje:detail', args=(personaje.id,)))
    else:
        return HttpResponseRedirect(reverse('fichapersonaje:detail', args=(personaje.id,)))