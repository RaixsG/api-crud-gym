from django.db import models

# Create your models here.
class TipoProducto(models.Model):
    
    tipo_producto = models.CharField(
        verbose_name = 'Tipo de Producto',
        max_length=30,
    )
    
    class Meta:
        ordering = ('id',)
        verbose_name = 'Tipo de Producto'
        verbose_name_plural = 'Tipos de Productos'

    def __str__(self):
        return self.tipo_producto

class Productos(models.Model):
    
    nombre = models.CharField(
        verbose_name = 'Nombre',
        max_length=50
    )
    descripcion = models.CharField(
        verbose_name = 'Descripcion',
        max_length=50
    )
    # image = models.ImageField(
    #     'Imagen del Producto',
    #     upload_to='productos/',
    #     blank=True,
    #     null=True
    # )
    precio = models.DecimalField(
        verbose_name = 'Precio',
        max_digits=5,
        decimal_places=2
    )
    stock = models.IntegerField(
        verbose_name = 'Stock',
        default=0
    )
    fecha_ingresada = models.DateTimeField(
        verbose_name = 'Fecha de Ingreso',
        auto_now=True
    )
    tipo_productos = models.ForeignKey(
        TipoProducto,
        on_delete=models.CASCADE,
        default='',
        blank = True,
        null = True
    )
    
    class Meta:
        ordering = ('id',)
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.nombre