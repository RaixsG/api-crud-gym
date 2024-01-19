from django.db import models

# Create your models here.
class Empleados(models.Model):
    TURNO_CHOICES = (
        ('M', 'Mañana'),
        ('T', 'Tarde'),
        ('N', 'Noche'),
    )
    
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
    turno = models.CharField(
        verbose_name = 'Turno',
        choices = TURNO_CHOICES,
        max_length=1
    )
    sueldo = models.DecimalField(
        verbose_name = 'Pago de sueldo',
        max_digits=6,
        decimal_places=2
    )

    def __str__(self):
        return self.nombres