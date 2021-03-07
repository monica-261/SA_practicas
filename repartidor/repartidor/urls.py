from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    #Se redirecciona para avisar al repartidor de un pedido
    path('', include('marcarEntrega.urls')),
    #Se redirecciona para informar del estado de un pedido
    path('', include('informarEstado.urls')),
    #Se redirecciona para recibir pedidos
    path('', include('recibirPedido.urls')),

]