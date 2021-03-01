from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime

# Se define que únicamente se utilizará el método get
@api_view(['GET'])

# Se define un método que recibe como parámetro un entero simulando una llave primaria
def estadoPedidoRestaurante(request, pk :int):
    # A través de un if, se válida si se recibe un request del tipo GET
    today = datetime.now()
    if request.method == 'GET':
        with open('logs.txt', 'w') as f:
            f.write(str(today) + ' El número de pedido '+ pk+ ' está siendo procesado\n')
        # Se imprime como respuesta la simulación del pedido.
        return Response("El pedido número " + pk + " está siendo peparado por el restaurante. ")
