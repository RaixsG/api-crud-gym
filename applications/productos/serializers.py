from rest_framework import serializers
from .models import (
    Productos,
    TipoProducto,
)

class AllTypeProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoProducto
        fields = (
            'id',
            'tipo_producto',
        )

class AllProductsSerializer(serializers.ModelSerializer):
    
    tipo_productos = AllTypeProductsSerializer(read_only=True)
    
    class Meta:
        model = Productos
        fields = ('__all__')

# Serializer Product video
# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Productos
#         exclude = ()