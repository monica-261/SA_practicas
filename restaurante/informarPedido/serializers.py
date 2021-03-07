from rest_framework import serializers
from .models import informarPedido

# Se crea un modelo para simular una base de datos
class informarPedidoSerilizer(serializers.ModelSerializer):
    class Meta:
        # Modelo que se va serializar 
        model = informarPedido 
        # Campos del modelo
        fields = ('producto', 'cantidad','estado')