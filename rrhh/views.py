from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required 
from . models import Empleado
from .forms import EmpleadoForm

@login_required
def lista_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'rrhh/lista_empleados.html', {'empleados': empleados})
#----------------------------------------------------------------------------------------------------------------------------------------------------
@login_required
def agregar_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rrhh:lista_empleados')
    else:
        form = EmpleadoForm()
    return render(request, 'rrhh/agregar_empleado.html', {'form': form})
#----------------------------------------------------------------------------------------------------------------------------------------------------

def inicio(request):
    return render(request, 'rrhh/inicio.html')