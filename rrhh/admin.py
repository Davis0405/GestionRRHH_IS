from django.contrib import admin
from .models import Departamento, Empleado, Nomina, Prestacion

admin.site.register(Departamento)
admin.site.register(Empleado)
admin.site.register(Nomina)
admin.site.register(Prestacion)