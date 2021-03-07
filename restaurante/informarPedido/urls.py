from django.urls import path
from .views import informarPedido

# Se declara la ruta por la cual se va a realizar el request POST 
urlpatterns = [
    path('informarPedido', informarPedido, name="informarPedido"),
]