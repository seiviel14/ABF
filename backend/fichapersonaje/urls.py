from django.urls import path

from . import views

app_name = "fichapersonaje"

urlpatterns = [
    #url.dom/FichaPersonaje/
    path('', views.personaje, name = 'personaje'),
    #url.dom/FichaPersonaje/2
    path('<int:pk>/', views.personajeDetail, name = 'detail'),
    #url.dom/FichaPersonaje/crearpersonaje/
    
]
'''path('crearpersonaje/', views.crearPersonaje, name = 'crearpersonaje'),
    #url.dom/FichaPersonaje/cambiardatos/2
    path('cambiardatos/<int:pk>/', views.CambiarDatosView.as_view(), name = 'cambiardatos'),
    
    path('cambiodatos/<int:personaje_id>/', views.cambioDatos, name = 'cambiodatos'),

    path('eliminarpersonaje/<int:personaje_id>/', views.eliminarPersonaje, name = 'eliminarpersonaje'),
    
    path('creardetalles/<int:personaje_id>', views.crearDetalles, name = 'creardetalles'),'''