from datetime import datetime,timedelta
import pandas as pd
import numpy as np

inicio = datetime.now()

registros = []

for i in range(0,15):

    timestamp = inicio + timedelta(minutes=i*10)


    # Sensor de temperatura. Simula lecturas de entre 0 y 40 grados. Se utilizan sensores DHT22
    temp = np.random.randint(0,40)

    # Sensor de luz. Simula luz ambiental en "lux". Sensor real LDR
    luz = np.random.randint(0,800)

    # Sensor de humedad. Simula humendad relativa entre 30 y 70 %. Sensor DHT22
    humedad = np.random.randint(0,100)

    # Sensor de CO2. Simula concentración entre 350 y 1200. Sensor real MH-Z19
    co = np.random.randint(350,1200)

    acciones = []

    
    if temp > 25:
        acciones.append("Encendiendo aire acondicionado")
    elif temp < 18:
        acciones.append("Encendiendo calefacción")
    else:
        acciones.append("Aire condicionado quitado")

    if luz < 200:
        acciones.append("Encendiendo luces")
    else:
        acciones.append("Apagando luces")

    if humedad < 40:
        acciones.append("Activando humidificador")
    elif humedad > 60:
        acciones.append("Desactivando humidificador")

    if co > 1000:
        acciones.append("Ventilando habitación")
    else:
        acciones.append("Puede cerrar las ventanas")
    
    registros.append({
        "Tiempo": timestamp.strftime("%Y-%m-%d %H:%M:%S"),
        "Temperatura":temp,
        "Luz" : luz,
        "Humedad %": humedad,
        "CO2": co,
        "Acciones: ": "; ".join(acciones)
    })

df = pd.DataFrame(registros)

df.to_csv("simulacion.csv")