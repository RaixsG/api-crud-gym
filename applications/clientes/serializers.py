from rest_framework import serializers
from .models import Clientes, ClientesFrecuentes

class AllClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields = (
            'id',
            'nombres',
            'apellidos',
            'dni',
            'celular',
            'fecha_inicio',
            'fecha_final',
            'mensualidad',
        )

class AllFrequentClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientesFrecuentes
        fields = (
            'id',
            'nombres',
            'celular',
            'fecha_ingresada',
            'pago',
        )

class TestSerializer(serializers.Serializer):
    nombres = serializers.CharField(max_length=200)
    dni = serializers.CharField(max_length=8)