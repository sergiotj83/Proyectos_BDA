# TAREAS

## Tarea 1. Creación de entidades

### Sensores Smart City – CO₂ y Calidad del Agua
```json
[
  {
    "id": "sensor2_co2",
    "tipo": "sensor_co2",
    "fecha_registro": {
      "type": "datetime",
      "valor": "2025-10-05T10:15:00Z",
      "unidad": "ISO 8601 (UTC)"
    },
    "atributos": {
      "co2":         { "type": "number", "valor": 820,  "unidad": "ppm" },
      "temperatura": { "type": "number", "valor": 23.4, "unidad": "°C"  },
      "humedad":     { "type": "number", "valor": 45.2, "unidad": "%"   },
      "presion":     { "type": "number", "valor": 1013.25, "unidad": "hPa" }
    }
  },
  {
    "id": "sensor3_calidad_agua",
    "tipo": "sensor_calidad_agua",
    "fecha_registro": {
      "type": "datetime",
      "valor": "2025-10-05T10:15:00Z",
      "unidad": "ISO 8601 (UTC)"
    },
    "atributos": {
      "ph":         { "type": "number", "valor": 7.3,  "unidad": "pH (adimensional)" },
      "temperatura":{ "type": "number", "valor": 21.5, "unidad": "°C" },
      "cloro":      { "type": "number", "valor": 0.45, "unidad": "mg/L" },
      "turbidez":   { "type": "number", "valor": 1.2,  "unidad": "NTU" }
    }
  }
]
```



## Tarea 2. Infraestructura FIWARE

### Petición POST de creación de las entidades
```
import requests
import json

# URL del endpoint de Orion
ORION_URL = "http://localhost:1026/v2/entities"

# Cabeceras HTTP
headers = {"Content-Type": "application/json"}

# Definición de las entidades a crear
entidades = [
    {
        "id": "sensor1_temp_humedad",
        "type": "sensor_temperatura_humedad",
        "dateObserved": {"type": "DateTime", "value": "2025-10-09T08:45:00Z"},
        "location": {
            "type": "geo:json",
            "value": {"type": "Point", "coordinates": [-0.4027, 39.5046]}
        },
        "temperatura": {"type": "Number", "value": 22.5},
        "humedad_relativa": {"type": "Number", "value": 45.2}
    },
    {
        "id": "sensor2_co2",
        "type": "sensor_co2",
        "dateObserved": {"type": "DateTime", "value": "2025-10-09T08:45:00Z"},
        "location": {
            "type": "geo:json",
            "value": {"type": "Point", "coordinates": [-0.4089, 39.5002]}
        },
        "co2": {"type": "Number", "value": 510},
        "temperatura": {"type": "Number", "value": 21.8},
        "humedad_relativa": {"type": "Number", "value": 48.6}
    },
    {
        "id": "sensor3_calidad_agua",
        "type": "sensor_calidad_agua",
        "dateObserved": {"type": "DateTime", "value": "2025-10-09T08:45:00Z"},
        "location": {
            "type": "geo:json",
            "value": {"type": "Point", "coordinates": [-0.3955, 39.5063]}
        },
        "ph": {"type": "Number", "value": 7.3},
        "temperatura": {"type": "Number", "value": 19.5},
        "cloro": {"type": "Number", "value": 1.1},
        "turbidez": {"type": "Number", "value": 4.5}
    }
]

# Creación de entidades
for e in entidades:
    print(f"Creación de {e['id']}...")
    response = requests.post(ORION_URL, headers=headers, data=json.dumps(e))
    if response.status_code == 201:
        print(f"Entidad {e['id']} creada correctamente.")
    elif response.status_code == 422:
        print(f" Entidad {e['id']} existente.")
    else:
        print(f"Error al crear {e['id']}: {response.status_code} - {response.text}")

print("\n Entdidades registradas en Orion:")
consulta = requests.get(ORION_URL)
print(json.dumps(consulta.json(), indent=4, ensure_ascii=False))
```
### Petición POST de creación de la suscripcion/es
```
import requests
import json


ORION_URL = "http://localhost:1026/v2/subscriptions"


headers = {"Content-Type": "application/json"}


suscripciones = [
    {
        "description": "Suscripción para sensor1_temp_humedad",
        "subject": {
            "entities": [{"id": "sensor1_temp_humedad", "type": "sensor_temperatura_humedad"}],
            "condition": {"attrs": ["temperatura", "humedad_relativa"]}
        },
        "notification": {
            "http": {"url": "http://quatum-leap:8668/v2/notify"},
            "attrs": ["temperatura", "humedad_relativa"],
            "metadata": ["dateCreated", "dateModified"]
        },
        "throttling": 1
    },
    {
        "description": "Suscripción para sensor2_co2",
        "subject": {
            "entities": [{"id": "sensor2_co2", "type": "sensor_co2"}],
            "condition": {"attrs": ["co2", "temperatura", "humedad_relativa"]}
        },
        "notification": {
            "http": {"url": "http://quatum-leap:8668/v2/notify"},
            "attrs": ["co2", "temperatura", "humedad_relativa"],
            "metadata": ["dateCreated", "dateModified"]
        },
        "throttling": 1
    },
    {
        "description": "Suscripción para sensor3_calidad_agua",
        "subject": {
            "entities": [{"id": "sensor3_calidad_agua", "type": "sensor_calidad_agua"}],
            "condition": {"attrs": ["ph", "temperatura", "cloro", "turbidez"]}
        },
        "notification": {
            "http": {"url": "http://quatum-leap:8668/v2/notify"},
            "attrs": ["ph", "temperatura", "cloro", "turbidez"],
            "metadata": ["dateCreated", "dateModified"]
        },
        "throttling": 1
    }
]


for s in suscripciones:
    print(f"Creación de suscripción: {s['description']}...")
    response = requests.post(ORION_URL, headers=headers, data=json.dumps(s))
    if response.status_code == 201:
        print(" Suscripción correcta.")
    elif response.status_code == 422:
        print("Suscripción existente.")
    else:
        print(f"Error creación de suscripción: {response.status_code} - {response.text}")


print("\n Listado de suscripciones:")
consulta = requests.get(ORION_URL)
print(json.dumps(consulta.json(), indent=4, ensure_ascii=False))



```

