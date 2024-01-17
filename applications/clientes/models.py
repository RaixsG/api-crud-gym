from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombres = models.CharField(
        verbose_name = 'nombres',
        max_length=50
    )
    apellidos = models.CharField(
        verbose_name = 'apellidos',
        max_length=50
    )
    dni = models.CharField(
        verbose_name = 'DNI',
        max_length=8,
        unique=True
    )
    celular = models.CharField(
        verbose_name = 'Numero de Celular',
        max_length=9
    )
    fecha_inicio = models.DateField(
        verbose_name = 'Fecha de Inscripción',
        auto_now=True
    )
    fecha_final = models.DateField()
    mensualidad = models.DecimalField(
        verbose_name = 'Pago de mensualidad',
        max_digits=5,
        decimal_places=2
    )
    
    class Meta:
        ordering = ('id',)
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nombres

class ClientesFrecuentes(models.Model):
    nombres = models.CharField(
        verbose_name = 'nombres',
        max_length=50
    )
    celular = models.CharField(
        verbose_name = 'Numero de Celular',
        max_length=9
    )
    fecha_ingresada = models.DateTimeField(
        verbose_name = 'Fecha de Inscripción',
        auto_now=True
    )
    pago = models.DecimalField(
        verbose_name = 'Pago',
        max_digits=5,
        decimal_places=2
    )
    
    class Meta:
        ordering = ('id',)
        verbose_name = 'Cliente Frecuente'
        verbose_name_plural = 'Clientes Frecuentes'

    def __str__(self):
        return self.nombres