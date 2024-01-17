from rest_framework import serializers
from .models import Empleados

class AllEmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleados
        fields = (
            'id',
            'nombres',
            'apellidos',
            'dni',
            'celular',
            'turno',
            'sueldo',
        )