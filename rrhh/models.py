from django.db import models

from django.db import models

class Departamento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'departamentos'
        managed = False

    def __str__(self):
        return self.nombre

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    puesto = models.CharField(max_length=100)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    fecha_contratacion = models.DateField()

    class Meta:
        db_table = 'empleados'
        managed = False

    def __str__(self):
        return self.nombre

class Nomina(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=20, choices=[('mensual', 'Mensual'), ('semanal', 'Semanal'), ('quincenal', 'Quincenal')])

    class Meta:
        db_table = 'nominas'

    def __str__(self):
        return f"{self.empleado.nombre} - {self.fecha}"

class Prestacion(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(blank=True, null=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        db_table = 'prestaciones'

    def __str__(self):
        return f"{self.empleado.nombre} - {self.tipo}"