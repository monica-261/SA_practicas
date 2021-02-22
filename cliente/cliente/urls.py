from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    #Se redirecciona para obtener el estado del pedido por parte del repartidor
    path('', include('estadoPedidoRepartidor.urls')),
    #Se redirecciona para obtener el estado del pedido por parte del restaurante
    path('', include('estadoPedidoRestaurante.urls')),
    #Se redirecciona para realizar el pedido
    path('', include('solicitarPedido.urls')),

]