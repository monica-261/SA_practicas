from django.urls import path
from .views import estadoPedidoRepartidor

# Se declara la ruta por la cual se va a realizar el request GET 
urlpatterns = [
    path('estadoPedidoRepartidor/<pk>/', estadoPedidoRepartidor, name="estadoPedidoRepartidor"),
]