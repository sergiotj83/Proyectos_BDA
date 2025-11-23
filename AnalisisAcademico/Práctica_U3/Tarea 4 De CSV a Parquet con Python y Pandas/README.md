# Tarea 4 – De CSV a Parquet con Python y Pandas

Esta carpeta contiene el script en Python utilizado para convertir los ficheros CSV limpios en formato Parquet.

El proceso se realiza para cada archivo limpio (`*_clean.csv`) del proyecto, generando un `.parquet` equivalente en la capa Oro.

A continuación se explica el funcionamiento del script y cómo se aplica a los diferentes archivos.
import pandas as pd
----------------------------------------------------------------------------------------
# El CSV está en la misma carpeta que este .py
ruta_csv = "calificaciones_limpio.csv"

df = pd.read_csv(ruta_csv)

df.to_parquet("calificaciones.parquet", index=False)

print("Conversión completada.")
------------------------------------------------------------------------
-Qué hace este código?

Importa la librería Pandas, necesaria para trabajar con ficheros CSV y Parquet.

Define la ruta del archivo CSV, en este caso uno llamado calificaciones_limpio.csv que debe estar en la misma carpeta que el script.

Lee el CSV y lo carga en un DataFrame (df).

Convierte el DataFrame a formato Parquet, un formato columnar comprimido ideal para análisis en la Capa Oro del Data Lakehouse.

Guarda el archivo resultante como calificaciones.parquet.

Muestra un mensaje por consola confirmando la conversión.

- ¿Por qué Parquet?

Es un formato columnar

Ocupa menos espacio

Es más rápido para análisis

Es compatible con herramientas modernas (NiFi, Spark, Databricks, AWS Glue, etc.)

-Objetivo en el proyecto

Este paso deja los datos listos para su uso en:

La Capa Oro

Procesos de BI

Indicadores anuales

Tablas de hechos del Data Warehouse
