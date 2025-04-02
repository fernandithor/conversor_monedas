"""
Este es un conversor de monedas que utiliza la API de ExchangeRate-API.
Permite al usuario convertir una moneda a otra con tasas de cambio en tiempo real.
"""
# Es un comentario en forma de docstring, que sirve como documentacion del programa. Explica
#brevemente qué hace el script. Es bueno documentar tu codigo.


import requests
# Importa la librería requests, que nos permite hacer solicitudes HTTP a la API de tasas
#de cambio.
# Usamos "requests" porque es una de las formas mas simpes y eficientes de obtener datos de una
#API en Python.


print(requests.__version__)  
# Muestra la versión de requests

moneda_origen = input("Introduce la moneda de origen (EUR): ").upper()
#Usa input() para pedir al usuario que escriba la moneda desde la cual quiere convertir (por ejemplo, USD o EUR).

def obtener_tasa_cambio(moneda_origen, moneda_destino):
#Define una funcion para obtener la tasa de cambio entre dos monedas desde la API.
#Nos permite reutilizar el código en diferentes partes del programa en lugar de escribirlo varias veces.

    url = f"https://api.exchangerate-api.com/v4/latest/{moneda_origen}"
    #Crea una URL con la moneda base que el usuario ingresa. 
    #Usamos f"{variable}" porque es una f-string, una forma eficiente de incluir variables
    #dentro de cadenas en Python.

    respuesta = requests.get(url)
    #Para hacer una peticion GET a la API y obtener los datos.
    #Es la forma mas sencilla de obtener datos desde una URL.

    if respuesta.status_code != 200:
        print("Error al obtener datos de la API")
        return None
    #Comprueba si la API responde correctamente (codigo 200). Si no, muestra un mensaje
    #de error y devuelve None. Es importante para evitar que el programa falle si la API
    #no está disponible.
    
    datos = respuesta.json()
    #Convierte la respuesta de la API en un diccionario Python, lo que nos permite
    # acceder a los datos fácilmente. 

    if moneda_destino in datos["rates"]:
        return datos["rates"][moneda_destino]
    else:
        print("Moneda no encontrada en la API")
        return None
    #Verifica si la moneda de destino esta en los datos y devuelve la tasa de cambio correspondiente.
    #Es importante para asegurarnos de que la moneda existe antes de continuar con los calculos.

    
def convertir_moneda():
#Def se usa para definir una funcion.
#convertir_moneda() es el nombre de la funcion que hemos creado.
#Vamos a definir una funcion llamada convertir_moneda, pero no se ejecuta automáticamente.
#Solo se ejecutará cuando la llamemos asi: convertir_moneda().
#Usamos la funcion para poder llamarla varias veces sin repetir codigo.

    moneda_origen = input("Introduce la moneda de origen (ej: USD, EUR): ").upper()
    #input() permite al usuario escribir un valor en la termina.
    #upper() convierte todo el texto a mayúsculas.
    moneda_destino = input("Introduce la moneda de destino (ej: USD, EUR): ").upper()
    #Estas dos lineas piden al usuario que ingrese la moneda de origen y la moneda de origen y destino

    tasa_cambio = obtener_tasa_cambio(moneda_origen, moneda_destino)
    #Usamos esta funcion para obtener la tasa de cambio de manera automatica desde una API
    #tasa_cambio almacena ese valor


    if tasa_cambio:
    #Esta linea comprueba si tasa_cambio tiene un valor válido.
    #Es necesario para saber si la API devolvió una tasa válida y podemos continuar.
        cantidad = float(input(f"Introduce la cantidad en {moneda_origen}: "))
        #Esta linea pide al usuario la cantidad de dinero a convertir.
        #float() convierte el texto ingresado en un número decimal.
        #input() muestra un mensaje en la terminal y espera que el usuario ingrese un valor
        #f"Introduce la cantidad en {moneda_origen}: ": crea un mensaje personalizado.
        #la letra "f" permite insertar variables en un string de forma sencilla.

        resultado = cantidad * tasa_cambio
        print(f"{cantidad} {moneda_origen} equivale a {resultado:.2f} {moneda_destino}")
        #Muestra el resultado de la conversión en pantalla.
        #Usa una f-string para incluir los valores en el texto.
        #{resultado:.2f}: redondea el número a 2 decimales.
        #Ejemplo de salida: 100 USD equivale a 85,00 EUR
        

# Ejecutar el conversor
convertir_moneda()

