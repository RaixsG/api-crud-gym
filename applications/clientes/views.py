from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
)
# Models
from .models import Clientes, ClientesFrecuentes
# Serializers
from .serializers import (
    AllClientsSerializer,
    AllFrequentClientsSerializer,
    TestSerializer,
)
# Create your views here.
class ListaClientes(viewsets.ModelViewSet):
    serializer_class = AllClientsSerializer
    
    queryset = Clientes.objects.all()
    Response(queryset, status=status.HTTP_200_OK)

class ListaClientesFrecuentes(ListAPIView):
    serializer_class = AllFrequentClientsSerializer
    
    queryset = ClientesFrecuentes.objects.all()

class CrearClienteFrecuentes(CreateAPIView):
    serializer_class = AllFrequentClientsSerializer