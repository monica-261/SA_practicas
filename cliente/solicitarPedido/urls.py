from django.urls import path
from .views import solicitarPedido

# Se declara la ruta por la cual se va a realizar el request POST 
urlpatterns = [
    path('solicitarPedido', solicitarPedido, name="solicitarPedido"),
    
]