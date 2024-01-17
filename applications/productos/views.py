from rest_framework import viewsets
from .models import (
    Productos,
    TipoProducto,
)
from .serializers import (
    AllProductsSerializer,
    AllTypeProductsSerializer,
)
# Create your views here.
class ListaProductos(viewsets.ModelViewSet):
    serializer_class = AllProductsSerializer
    
    queryset = Productos.objects.all()

class ListaTipoProductos(viewsets.ModelViewSet):
    serializer_class = AllTypeProductsSerializer
    
    queryset = TipoProducto.objects.all()