# Practica 3
______

## Ejecución del proyecto
> Se debe de tener instalado Python en su versión 3.8.6.

> Se debe tener instalado DJango 

> En la carpeta de cada microservicio ejecutar `> pip install djangorestframework`

> Ejecutar desde la terminal, en la carpeta del microservicio por ejecutar, el comando `> python manage.py runserver`

## Pruebas de funcionalidad

### Para el microservicio de CLIENTE 
- Se ejecuta el comando `> python manage.py runserver`

![image](https://user-images.githubusercontent.com/12808348/108665006-8b405700-7499-11eb-9dad-7cbebc170e7f.png)

- A través de la URL `http://127.0.0.1:8000/estadoPedidoRepartidor/1/` se consulta el estado del pedido por parte del repartidor 

![image](https://user-images.githubusercontent.com/12808348/108665123-cb073e80-7499-11eb-99a1-4332b884cb3e.png)

Se observa que se obtiene como respuesta `"El pedido número 1 está en ruta"` siendo el pedido 1 el consultado

- A través de la URL `http://127.0.0.1:8000/estadoPedidoRestaurante/1/` se consulta el estado del servicio 

![image](https://user-images.githubusercontent.com/12808348/108665227-10c40700-749a-11eb-9e06-981d9c9f37b7.png)

Se observa que se obtiene como respuesta `"El pedido número 1 está en ruta"` siendo el pedido 1 el consultado

- A través de la URL `http://127.0.0.1:8000/solicitarPedido` se hace la solicitud a través del método POST para un pedido 

![image](https://user-images.githubusercontent.com/12808348/108665344-52ed4880-749a-11eb-8ac1-417ac5156816.png)

Se hace la solicitud a través del JSON 

`
{
"producto": "Bebida",
"cantidad": "5"
}`
    
Dado sea el caso la solicitud sea correctamente estructurada, se obtiene el mensaje 

![image](https://user-images.githubusercontent.com/12808348/108665424-7f08c980-749a-11eb-8e43-ceb2811e6caf.png)

> ___Nota: Para las demás microservicios, es la misma operativa. Lo único que cambia es JSON enviado por microservicio. En donde: ___

### Para marcarEntrega (repartidor)

{
"pedido": "1",
"entrega": "terminado"
}
    
### Para informarEstado (repartidor) e informarPedido (restaurante)

{
"producto": "Bebida",
"cantidad": "5",
"estado": "preparando"
}
    
### Para avisarRepartidor (restaurante)

{
"producto": "Bebida",
"cantidad": "5",
"restaurante": "La quinta"
}
    
