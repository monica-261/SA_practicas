from rest_framework import serializers
from .models import avisarRepartidor

# Se crea un modelo para simular una base de datos
class avisarRepartidorSerializer(serializers.ModelSerializer):
    class Meta:
        # Modelo que se va serializar 
        model = avisarRepartidor 
        # Campos del modelo
        fields = ('producto', 'cantidad','restaurante')