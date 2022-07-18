
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import render, get_object_or_404

from .models import Personaje#, Caracteristica, Secundaria
from .static.fichapersonaje.tablas.tablas import campos_secundarias, secundarias_caracteristicas
from .serializers import PersonajeSerializer

def front(request):
    context = {}
    return render(request, 'index.html', context)

@api_view(['GET', 'POST'])
def personaje(request):
    if request.method == 'GET':
        personaje = Personaje.objects.all()
        serializer = PersonajeSerializer(personaje, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PersonajeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE', 'GET'])
def personajeDetail(request, pk):
    try:
        personaje = get_object_or_404(Personaje, pk=pk)
    except Personaje.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        personaje.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'GET':
        serializer = PersonajeSerializer(personaje)
        return Response(serializer.data)

'''# Create your views here.
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

def crearDetalles(request, personaje_id):
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
        return HttpResponseRedirect(reverse('fichapersonaje:detail', args=(personaje.id,)))

def crearDetalles(request, personaje_id):
    personaje = get_object_or_404(Personaje, pk=personaje_id)
    if not Caracteristica.objects.filter(personaje=personaje):
        for nombre_caracteristica in secundarias_caracteristicas:
            Caracteristica.objects.create(personaje=personaje,nombre_caracteristica=nombre_caracteristica )
            caracteristica = Caracteristica.objects.get(personaje=personaje,nombre_caracteristica=nombre_caracteristica )

            for secundaria in secundarias_caracteristicas[nombre_caracteristica]:
                campo_secundaria = [campo for campo, secundarias in campos_secundarias.items() for secundaria_nombre in secundarias if secundaria_nombre == secundaria]
                Secundaria.objects.create(personaje=personaje, caracteristica=caracteristica,nombre_secundaria=secundaria, campo=campo_secundaria[0])

        for campo in campos_secundarias:
            for secundaria in campos_secundarias[campo]:
                caracteristica_secundaria = [caracteristica for caracteristica, secundarias in secundarias_caracteristicas.items() for secundaria_nombre in secundarias if secundaria_nombre == secundaria]
                caracteristica = get_object_or_404(Caracteristica, personaje = personaje, nombre_caracteristica = caracteristica_secundaria[0])
                Secundaria.objects.create(personaje = personaje, caracteristica = caracteristica, nombre_secundaria = secundaria, campo = campo)

        return HttpResponseRedirect(reverse('fichapersonaje:detail', args=(personaje.id,)))
    else:
        return HttpResponseRedirect(reverse('fichapersonaje:detail', args=(personaje.id,)))'''