import os
import msvcrt as p
import random
import json
import base64
header = {"alg": "HS256", "typ": "JWT"}
tokens ={}

# Método para generar el secret asociado
def generarSecret():
    secret = ''
    i = 0
    while i<15:
        op = random.randint(1, 3)
        if op == 1:
            # random para añadir al secrete letras de la A - Z en mayúsculas
            secret += str(chr(random.randint(65,90)))
        elif op == 2:
            # random para añadir al secret letras de la A - Z en minúsculas
            secret += str(chr(random.randint(97,122)))            
        elif op == 3:
            # random para añadir al secret digitos del 0 al 9
            secret += str(chr(random.randint(48,57)))
        i = i + 1
    return secret



# Método de menu para que el programa continue hasta que se presiona la opción 3    
def menu():
    opcion = input("Ingrese su opción: \n 1. Codificar \n 2. Decodificar \n 3. Salir \n")
    if opcion == '1':
        codificar()
    elif opcion == '2':
        decodificar()
    elif opcion == '3':
        return

# Método para esperar que el usuario ingrese una tecla y continuar con el flujo del programa
def pausa():
    p.getch()

# Método que retorna el token codificado
def codificar():
    # Se solicita el carnet para codificar 
    valorCarnet = input("Ingrese su carnet: ")
    # A través de un try se valida que el carnet sea del tipo númerico, caso contrario falla
    try:
       carnet = int(valorCarnet)
    except ValueError:
        # Dado caso el carnet no sea númerico se muestra una alerta
        print("El carnet debe de ser un número")
        # Se pausa el programa a la espera de ingresar una letra
        pausa()
        # Se vuelve a pedir un nuevo carnet
        codificar()
    # Si el carnet es válido, se solicita el nombre del usuario
    nombre = input("Ingrese su nombre: ")
    # Se almacena en un JSON el valor del secret
    tokens[carnet]=generarSecret()
    # Se codifica en header
    h = str(header).encode('ascii')
    # Se convierte en base 64
    header64 = base64.b64encode(h)
    # Se decodifica el header
    hm = header64.decode('ascii')
    # Se genera un JSON para el cuerpo del JWT
    body = {"carnet": carnet,"nombre":nombre}
    # Se codifica en ascci
    c = str(body).encode('ascii')
    # Se codifica en base64
    c64 = base64.b64encode(c)
    # Se decodifica a base ascii el codificado a base64
    cm = c64.decode('ascii')
    # Se decodifica del JSON el valor de carnet
    s = str(tokens[carnet]).encode('ascii')
    # Se codifica a base64
    s64 = base64.b64encode(s)
    # Se decodifica 
    sm = s64.decode('ascii')
    # Se imprime el token obtenido
    print("El token es: " + hm+"."+cm+"."+sm)
    menu()

    
# Método para codificar y validar el JWT
def decodificar():
    # Se solicita el token para validar
    llave = input("Ingrese el token para decodificar:\n")
    try:
        # Se realiza un split al texto hasta cada punto
        txt = llave.split(".")
        # Se obtiene el header y se codifica a ascii
        h164 = str(txt[0]).encode('ascii')
        # Se obtiene el body y se codifica a ascii
        c164 = str(txt[1]).encode('ascii')
        # Se decodifica el body de base64 
        cb1 = base64.b64decode(c164)
        # Se decodifica el base64 obtenido de base ascii
        cm1 = cb1.decode('ascii')
        # Se decodifica el secret de ascii
        s164 = str(txt[2]).encode('ascii')
        # Se convierte en un diccionario
        dic = json.loads(cm1.replace("'",'"'))
        try:
            # Se valida que el carnet obtenido se encuentra en la lista
            if dic['carnet'] in tokens:
                #Si se encuentra se decodifica el header
                h = str(header).encode('ascii')
                h64 = base64.b64encode(h)
                hm = h64.decode('ascii')
                # Se almacena el carnet y el nombre obtenido de la decodificación
                cuerpo = {"carnet": dic['carnet'], "nombre": dic['nombre']}
                # Se vuelve a codificar el cuerpo a base ascii
                c = str(cuerpo).encode('ascii')
                # Nuevamente se decodifica a base64
                c64 = base64.b64encode(c)
                # De base64 se decodifica a ascii
                cm = c64.decode('ascii')
                # Se almacena en un string el token carnet codificado a ascii
                s = str(tokens[dic['carnet']]).encode('ascii')
                # Se decodifica de base64 el string
                s64 = base64.b64encode(s)
                # Se codifica a ascii
                sm = s64.decode('ascii')
                # Se forma un nuevo string conformado del header, el body y el secret
                llave2 = hm + '.' + cm + '.' + sm
                # Se compara si el valor obtenido del token JWT es igual al existente en memoria
                # Caso contrario es token inválido
                if llave2 == llave:
                    print("Token Valido")
                else:
                    print("Token Invalido")
            else:
                print("Carnet no ha sido procesado")
        except:
                print("Llave ingresada no tiene atributo carnet")
    except:
        print("Token no valido")
    menu()
        
if __name__ == '__main__':
    menu()