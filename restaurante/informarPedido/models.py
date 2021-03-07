from django.db import models

# Se genera un modelado de base de datos para simular el pedido
class informarPedido(models.Model):
   producto = models.CharField(max_length=20)
   cantidad = models.CharField(max_length=20)
   estado = models.CharField(max_length=20)
   added_on = models.DateTimeField(auto_now_add=True)
   
   def __str__(self):
       return self.pr