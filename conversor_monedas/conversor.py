"""
Este es un conversor de monedas que utiliza la API de ExchangeRate-API.
Permite al usuario convertir una moneda a otra con tasas de cambio en tiempo real.
"""
import requests

print(requests.__version__)  # Muestra la versión de requests

moneda_origen = input("Introduce la moneda de origen (EUR): ").upper()
#Usa input() para pedir al usuario que escriba la moneda desde la cual quiere convertir (por ejemplo, USD o EUR).

def obtener_tasa_cambio(moneda_origen, moneda_destino):
    url = f"https://api.exchangerate-api.com/v4/latest/{moneda_origen}"
    respuesta = requests.get(url)

    if respuesta.status_code != 200:
        print("Error al obtener datos de la API")
        return None
    
    datos = respuesta.json()

    if moneda_destino in datos["rates"]:
        return datos["rates"][moneda_destino]
    else:
        print("Moneda no encontrada en la API")
        return None
    
def convertir_moneda():
    moneda_origen = input("Introduce la moneda de origen (ej: USD, EUR): ").upper()
    moneda_destino = input("Introduce la moneda de destino (ej: USD, EUR): ").upper()

    tasa_cambio = obtener_tasa_cambio(moneda_origen, moneda_destino)

    if tasa_cambio:
        cantidad = float(input(f"Introduce la cantidad en {moneda_origen}: "))
        resultado = cantidad * tasa_cambio
        print(f"{cantidad} {moneda_origen} equivale a {resultado:.2f} {moneda_destino}")

# Ejecutar el conversor
convertir_moneda()

