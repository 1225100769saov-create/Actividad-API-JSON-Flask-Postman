import requests

def obtener_clima(latitud, longitud):
    url = "https://api.open-meteo.com/v1/forecast"
    parametros = {
        "latitude": latitud,
        "longitude": longitud,
        "current": "temperature_2m,wind_speed_10m"
    }
    r = requests.get(url, params=parametros, timeout=10)
    r.raise_for_status()
    datos = r.json()["current"]
    
    return {
        "temperatura": datos["temperature_2m"],
        "viento": datos["wind_speed_10m"]
    }

# Definición de las 3 ciudades
ciudades = [
    {"nombre": "Querétaro", "lat": 20.59, "lon": -100.39},
    {"nombre": "Ciudad de México", "lat": 19.43, "lon": -99.13},
    {"nombre": "Guadalajara", "lat": 20.67, "lon": -103.35}
]

# Imprimir resultados en forma de tabla
print(f"{'Ciudad':<18} | {'Temp (°C)':<10} | {'Viento (km/h)':<12}")
print("-" * 46)

for c in ciudades:
    clima = obtener_clima(c["lat"], c["lon"])
    print(f"{c['nombre']:<18} | {clima['temperatura']:<10} | {clima['viento']:<12}")

print("\nSamuel Antonio Olvera Villegas")