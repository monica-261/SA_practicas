from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import avisarRepartidor
from .serializers import avisarRepartidorSerializer

#Se define que se pueden recibir métodos tanto GET como POST
@api_view(['GET', 'POST'])
def avisarRepartidor(request):
    # A través de un if, se válida si se va a realizar una petición GET
    if request.method == 'GET': 
        # Se deja definido que se consulte los datos de la base de datos
        return Response("serializer.data")
    # Se válida si la petición es un post
    elif request.method == 'POST': 
        # Se crea un objeto de tipo serializer en el cual se hará un request con los datos 
        serializer = avisarRepartidorSerializer(data=request.data)
        # Se válida si la petición es correcta
        if serializer.is_valid():
            # Si la petición es correcta, se responde con el número de éxito 201 y se indica que el pedido se ha realizado correctamente
            return Response('El repartidor se ha avisado con éxito', status=status.HTTP_201_CREATED)
        # Si la petición no es correcta, se responde con el número 400 de solicitud incorrecta    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)