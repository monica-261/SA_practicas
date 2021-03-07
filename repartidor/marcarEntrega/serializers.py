from rest_framework import serializers
from .models import marcarEntrega

# Se crea un modelo para simular una base de datos
class marcarEntregaSerializers(serializers.ModelSerializer):
    class Meta:
        # Modelo que se va serializar 
        model = marcarEntrega 
        # Campos del modelo
        fields = ('pedido', 'entrega')