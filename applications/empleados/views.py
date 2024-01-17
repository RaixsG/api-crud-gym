from rest_framework import viewsets
from .models import Empleados
# serializers
from .serializers import AllEmployeesSerializer

# Create your views here.
class ListaEmpleados(viewsets.ModelViewSet):
    serializer_class = AllEmployeesSerializer
    
    queryset = Empleados.objects.all()