from django.urls import path
from .views import recibirPedido

# Se declara la ruta por la cual se va a realizar el request GET 
urlpatterns = [
    path('recibirPedido/<pk>/', recibirPedido, name="recibirPedido"),
    
]