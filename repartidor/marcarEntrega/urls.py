from django.urls import path
from .views import marcarEntrega

# Se declara la ruta por la cual se va a realizar el request GET 
urlpatterns = [
    path('marcarEntrega', marcarEntrega, name="marcarEntrega"),
    
]