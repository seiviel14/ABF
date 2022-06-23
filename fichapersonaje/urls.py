from django.urls import path

from . import views

app_name = "fichapersonaje"

urlpatterns = [
    #url.dom/FichaPersonaje/
    path('', views.IndexView.as_view(), name = 'index'),
    #url.dom/FichaPersonaje/2
    path('<int:pk>/', views.PersonajeView.as_view(), name = 'detail'),
    #url.dom/FichaPersonaje/crearpersonaje/
    path('crearpersonaje/', views.crearPersonaje, name = 'crearpersonaje'),
    #url.dom/FichaPersonaje/cambiardatos/2
    path('cambiardatos/<int:personaje_id>/', views.cambiarDatos, name = 'cambiardatos'),
    
]
