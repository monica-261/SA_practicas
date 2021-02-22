from django.urls import path
from .views import informarEstado

# Se declara la ruta por la cual se va a realizar el request POST 
urlpatterns = [
    path('informarEstado', informarEstado, name="informarEstado"),
]