from django.urls import path
from turnos import views

urlpatterns = [
    path('', views.reservar_turno, name='home'),
    path('guardar/', views.comprobar_formulario),
    path('confirmar/', views.guardar_datos, name='guardar'), 
]
