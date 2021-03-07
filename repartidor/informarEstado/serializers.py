from rest_framework import serializers
from .models import informarEstado

# Se crea un modelo para simular una base de datos
class informarEstadoSerilizer(serializers.ModelSerializer):
    class Meta:
        # Modelo que se va serializar 
        model = informarEstado 
        # Campos del modelo
        fields = ('producto', 'cantidad','estado')