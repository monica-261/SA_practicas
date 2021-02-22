from rest_framework import serializers
from .models import solicitarPedido

# Se crea un modelo para simular una base de datos
class solicitarPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        # Modelo que se va serializar 
        model = solicitarPedido 
        # Campos del modelo
        fields = ('producto', 'cantidad')