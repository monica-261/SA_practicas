from django.urls import path
from .views import avisarRepartidor

# Se declara la ruta por la cual se va a realizar el request POST 
urlpatterns = [
    path('avisarRepartidor', avisarRepartidor, name="avisarRepartidor"),
]