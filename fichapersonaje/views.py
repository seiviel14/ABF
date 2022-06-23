from audioop import reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Personaje

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
