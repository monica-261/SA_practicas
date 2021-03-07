from django.urls import path
from .views import estadoPedidoRestaurante

# Se declara la ruta por la cual se va a realizar el request GET 
urlpatterns = [
    path('estadoPedidoRestaurante/<pk>/', estadoPedidoRestaurante, name="estadoPedidoRestaurante"),
    
]