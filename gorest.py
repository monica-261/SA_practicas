# Importación de la libreria requests
import requests

# Variable que contiene el endpoint del servicio por consumir
endPoint = "https://gorest.co.in/public-api/users"

# Metodo para actualizar el usuario
def actualizarUsuario():
    # Variable de tipo input la cual permite al usuario ingresar  el correo a buscar, se utiliza el correo ya que es llave primaria
    correo = input("Ingrese el correo del usuario que por modificar \n")
    # Variable de tipo json que almacena el email ingresado por el usuario
    email = {'email':correo} 
    # Variable de tipo requests que realiza la solicitud tipo get
    get = requests.get(url = endPoint, params = email)
    # Se transforma la respuesta en un json
    data = get.json()
    # Se obtiene el identificador 
    idUsuario = data['data'][0]['id']
    # Variable que contiene el endpoint con el id del usuario
    endPoint1 = endPoint + '/' + str(idUsuario)
    # Variable de autenticación 
    apiKey = {"Authorization": "Bearer ae04b3eb4c8d8bba02a0306e15035def8035ca96772ee372311b55ca7e97922f"}
    # Variable de tipo input que permite ingresar al usuario el nuevo nombre
    nombre = input("Ingrese el nuevo nombre \n")
    # Variable tipo json que almacena el nombre actualizado
    data = { "name": nombre}
    # Variable tipo request que realiza la solicitud tipo put
    put = requests.put(url = endPoint1, data = data, headers = apiKey) 
    print("Se modifico el usuario") 

# Metodo para crear el usuario
def crearUsuario():
    # Variable de autenticación 
    apiKey = {"Authorization": "Bearer ae04b3eb4c8d8bba02a0306e15035def8035ca96772ee372311b55ca7e97922f"}
    # Variable tipo json que almacena los datos para dar de alta
    requestPost = { "name": "rCalderon", "email" : "monicalderon@gmail.com", "gender" : "Female", "status" : "Active" }
    # Variable tipo request que realiza la solicitud tipo post
    postRequest = requests.post(url = endPoint, data = requestPost, headers = apiKey) 
    # Se transforma la respuesta en un json
    data = postRequest.json()
    # Se imprime la respuesta para verificar que todo haya ido bien
    print(data)

# Metodo para eliminar el usuario
def eliminarUsuario():
    # Variable de tipo input la cual permite al usuario ingresar  el correo a buscar, se utiliza el correo ya que es llave primaria
    email = input("Ingrese el correo del usuario que va a eliminar \n")
    # Variable de tipo json que almacena el email ingresado por el usuario
    usuario = {'email':email} 
    # Variable tipo request que realiza la solicitud tipo get
    request = requests.get(url = endPoint, params = usuario) 
    # Se transforma la respuesta en un json
    data = request.json() 
    # Se obtiene el identificador 
    idUsuario = data['data'][0]['id']
    # Variable que contiene el endpoint con el id del usuario
    endPoint1 = endPoint +'/'+ str(idUsuario)
    # Variable de autenticación 
    apiKey = {"Authorization": "Bearer ae04b3eb4c8d8bba02a0306e15035def8035ca96772ee372311b55ca7e97922f"}
    # Variable tipo request que realiza la solicitud tipo delete
    delete = requests.delete(url = endPoint1, headers = apiKey)
    # Se transforma la respuesta en un json
    data = delete.json()
    # Se imprime la respuesta para verificar que todo haya ido bien
    print(data) 


# Metodo para mostrar el usuario
def mostrarUsuario():
    # Variable de tipo input la cual permite al usuario ingresar  el correo a buscar, se utiliza el correo ya que es llave primaria
    correo = input("Ingrese el correo del usuario que va a mostrar \n")
    # Variable de tipo json que almacena el email ingresado por el usuario
    usuario = {'email':correo} 
    # Variable tipo request que realiza la solicitud tipo get
    get = requests.get(url = endPoint, params = usuario) 
    # Se transforma la respuesta en un json
    data = get.json() 
    # Se valida que el atributo data no venga vacio
    # Si no viene vacio, se imprime los valores 
    if len(data['data'])==0:
        print("No existe el usuario")
    else: 
        name = data['data'][0]['name']
        email = data['data'][0]['email']
        gender = data['data'][0]['gender']
        print("Nombre:%s\nEmail:%s\nGender:%s"
        %(name , email,gender)) 




# Variable de tipo input la cual permite al usuario ingresar un número para seleccionar la acción que desea hacer 
opcion = input("Ingrese el número de opción para realizar: \n 1. Crear usuario \n 2. Actualizar usuario \n 3. Mostrar usuario \n 4. Eliminar usuario \n")

# Acción de crear el usuario
if opcion == str(1):
    crearUsuario()
# Acción de actualizar el usuario
elif opcion == str(2):
    actualizarUsuario()
# Acción de mostrar el usuario
elif opcion == str(3):
    mostrarUsuario()
# Acción de eliminar el usuario
elif opcion == str(4):
    eliminarUsuario()
