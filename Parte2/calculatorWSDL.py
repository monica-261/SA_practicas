# Se importa la librería request
import requests

# Método para sumar
def suma():
    # URL por consumir
    url="http://www.dneonline.com/calculator.asmx?wsdl/Add"
    # Se declaran los headers indicando el tipo de contenido
    headers = {'content-type': 'text/xml'}
    # Se declara el cuerpo a envíar
    body = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tem="http://tempuri.org/">
    <soapenv:Header/>
    <soapenv:Body>
        <tem:Add>
            <tem:intA>"""+ intA +"""</tem:intA>
            <tem:intB>"""+ intB + """</tem:intB>
        </tem:Add>
    </soapenv:Body>
    </soapenv:Envelope>"""
    # Se almacena en un objeto la respuesta del POST
    response = requests.post(url,data=body,headers=headers)
    # Se imprime la respuesta del servicio
    print (response.content)

# Método para sumar
def resta():
    # URL por consumir
    url="http://www.dneonline.com/calculator.asmx?wsdl/Subtract"
    # Se declaran los headers indicando el tipo de contenido
    headers = {'content-type': 'text/xml'}
    # Se declara el cuerpo a envíar
    body = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tem="http://tempuri.org/">
    <soapenv:Header/>
    <soapenv:Body>
        <tem:Subtract>
            <tem:intA>"""+ intA +"""</tem:intA>
            <tem:intB>"""+ intB + """</tem:intB>
        </tem:Subtract>
    </soapenv:Body>
    </soapenv:Envelope>"""
    # Se almacena en un objeto la respuesta del POST
    response = requests.post(url,data=body,headers=headers)
    # Se imprime la respuesta del servicio
    print (response.content)

# Método para multiplicar
def mult():
    # URL por consumir
    url="http://www.dneonline.com/calculator.asmx?wsdl/Multiply"
    # Se declaran los headers indicando el tipo de contenido
    headers = {'content-type': 'text/xml'}
    # Se declara el cuerpo a envíar
    body = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tem="http://tempuri.org/">
    <soapenv:Header/>
    <soapenv:Body>
        <tem:Multiply>
            <tem:intA>"""+ intA +"""</tem:intA>
            <tem:intB>"""+ intB + """</tem:intB>
        </tem:Multiply>
    </soapenv:Body>
    </soapenv:Envelope>"""
    # Se almacena en un objeto la respuesta del POST
    response = requests.post(url,data=body,headers=headers)
    # Se imprime la respuesta del servicio
    print (response.content)

# Método para dividir
def div():
    # URL por consumir
    url="http://www.dneonline.com/calculator.asmx?wsdl/Divide"
    # Se declaran los headers indicando el tipo de contenido
    headers = {'content-type': 'text/xml'}
    # Se declara el cuerpo a envíar
    body = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tem="http://tempuri.org/">
    <soapenv:Header/>
    <soapenv:Body>
        <tem:Divide>
            <tem:intA>"""+ intA +"""</tem:intA>
            <tem:intB>"""+ intB + """</tem:intB>
        </tem:Divide>
    </soapenv:Body>
    </soapenv:Envelope>"""
    # Se almacena en un objeto la respuesta del POST
    response = requests.post(url,data=body,headers=headers)
    # Se imprime la respuesta del servicio
    print (response.content)

# Se solicita el primer número para operar
intA = input("Ingrese el número A: ")
# Se solicita el segundo número para operar
intB = input("Ingrese el número B: ")

# Se imprime un menú con las opciones disponibles
opcion= input("¿Que operación desea realizar? \n 1. Suma \n 2. Resta \n 3. Multiplicación \n 4. División \n")

# Se realiza un if con las opciones que el usuario puede escoger
if opcion == str(1):
    suma()
elif opcion == str(2):
    resta()
elif opcion == str(3):
    mult()
elif opcion == str(4):
    div()