from django.db import models

	# Se genera un modelado de base de datos para simular el pedido
class marcarEntrega(models.Model):
	pedido = models.CharField(max_length=20)
	entrega = models.CharField(max_length=20)
	added_on = models.DateTimeField(auto_now_add=True)
	   
	def __str__(self):
	    return self.pr