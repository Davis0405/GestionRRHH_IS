from django.urls import path
from . import views

app_name = 'rrhh'

urlpatterns = [
    path('empleados/', views.lista_empleados, name='lista_empleados'),
    path('inicio/', views.inicio, name='inicio'),  # Ejemplo de vista de inicio
    path('agregar_empleado/', views.agregar_empleado, name='agregar_empleado'),
]