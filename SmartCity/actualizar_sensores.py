'''
# PATCH_UPDATE.py
import requests
import json
from datetime import datetime, timedelta
import random
import pandas as pd
import time


# CONFIGURACIÓN GENERAL

HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json",
}

# Contról de errores
def enviar_patch(url, datos):
    try:
        respuesta = requests.patch(url, headers=HEADERS, data=json.dumps(datos))
        if respuesta.status_code == 204:
            return True
        else:
            print(f"Error {respuesta.status_code}: {respuesta.text[:100]}")
            return False
    except Exception as e:
        print(f"Excepción al conectar con Orion: {e}")
        return False



# SENSOR 1: temperatura + humedad

def sensor1_temp_humedad():
    ORION_URL = "http://localhost:1026/v2/entities/sensor1_temp_humedad/attrs"

    fecha = datetime(2025, 1, 1, 0, 0, 0)
    registros = []

    for i in range(400):
        dateObserved = fecha.isoformat() + "Z"
        temperatura = round(random.uniform(-10.0, 45.0), 1)
        humedad_relativa = round(random.uniform(20.0, 90.0), 1)

        datos = {
            "dateObserved": {"type": "DateTime", "value": dateObserved},
            "temperatura": {"type": "Number", "value": temperatura},
            "humedad_relativa": {"type": "Number", "value": humedad_relativa},
        }

        ok = enviar_patch(ORION_URL, datos)
        if ok:
            print(f"Sensor1 Día {i+1}/400 - {dateObserved}")
        else:
            print(f"Error Sensor1 en día {i+1}")

        registros.append(datos)
        fecha += timedelta(days=1)
        time.sleep(1)

    df = pd.DataFrame(registros)
    print("\n[Resumen sensor1_temp_humedad]")
    print(df.tail(5))



# SENSOR 2: CO₂ + temperatura + humedad

def sensor2_co2():
    ORION_URL = "http://localhost:1026/v2/entities/sensor2_co2/attrs"

    fecha = datetime(2025, 1, 1, 0, 0, 0)
    registros = []

    for i in range(400):
        dateObserved = fecha.isoformat() + "Z"
        co2 = int(random.uniform(400, 2000))
        temperatura = round(random.uniform(-10, 45.0), 1)
        humedad_relativa = round(random.uniform(20.0, 90.0), 1)

        datos = {
            "dateObserved": {"type": "DateTime", "value": dateObserved},
            "co2": {"type": "Number", "value": co2},
            "temperatura": {"type": "Number", "value": temperatura},
            "humedad_relativa": {"type": "Number", "value": humedad_relativa},
        }

        ok = enviar_patch(ORION_URL, datos)
        if ok:
            print(f"Sensor2 Día {i+1}/400 - {dateObserved}")
        else:
            print(f"Error Sensor2 en día {i+1}")

        registros.append(datos)
        fecha += timedelta(days=1)
        time.sleep(1)

    df = pd.DataFrame(registros)
    print("\n[Resumen sensor2_co2]")
    print(df.tail(5))



# SENSOR 3: calidad del agua (pH, temperatura, cloro, turbidez)

def sensor3_calidad_agua():
    ORION_URL = "http://localhost:1026/v2/entities/sensor3_calidad_agua/attrs"

    fecha = datetime(2025, 1, 1, 0, 0, 0)
    registros = []

    for i in range(400):
        dateObserved = fecha.isoformat() + "Z"
        ph = round(random.uniform(6.5, 8.0), 2)
        temperatura = round(random.uniform(-10.0, 45.0), 1)
        cloro = round(random.uniform(0.2, 1.5), 2)
        turbidez = round(random.uniform(0.1, 6.0), 2)

        datos = {
            "dateObserved": {"type": "DateTime", "value": dateObserved},
            "ph": {"type": "Number", "value": ph},
            "temperatura": {"type": "Number", "value": temperatura},
            "cloro": {"type": "Number", "value": cloro},
            "turbidez": {"type": "Number", "value": turbidez},
        }

        ok = enviar_patch(ORION_URL, datos)
        if ok:
            print(f"Sensor3 Día {i+1}/400 - {dateObserved}")
        else:
            print(f"Error Sensor3 en día {i+1}")

        registros.append(datos)
        fecha += timedelta(days=1)
        time.sleep(1)

    df = pd.DataFrame(registros)
    print("\n[Resumen sensor3_calidad_agua]")
    print(df.tail(5))



# EJECUCIÓN

sensor1_temp_humedad()
sensor2_co2()
sensor3_calidad_agua()
'''
