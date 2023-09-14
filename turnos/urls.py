from django.urls import path
from turnos import views

urlpatterns = [
    path('', views.reservar_turno, name='home'),
    path('success/', views.success, name='success')
]
