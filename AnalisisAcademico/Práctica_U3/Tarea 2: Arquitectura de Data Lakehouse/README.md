# Arquitectura Medallón (Bronce – Plata – Oro)

A continuación se describe la arquitectura en capas para el proyecto Análisis Académico siguiendo el modelo Medallón:

## 🟫 Capa Bronce (Raw)
- Datos originales tal como salen de ÍTACA y actas
- Se almacenan en CSV
- Pueden contener errores, nulos, duplicados o inconsistencias
- Ejemplos: alumnos_raw.csv, calificaciones_raw.csv, cursos_raw.csv

## 🥈 Capa Plata (Clean)
- Datos limpios y validados
- Tipado correcto (números, fechas, categorías)
- Normalización de nombres y claves
- Validación de rangos de notas
- Eliminación de duplicados
- Imputación de nulos
- Resultado: alumnos_clean.csv, calificaciones_clean.csv, etc.

## 🥇 Capa Oro (Processed)
- Datos modelados y listos para BI
- Formato Parquet (columnar)
- Esquema en estrella (dimensiones + hechos)
- Fact_Calificaciones.parquet
- Dim_Alumnos.parquet, Dim_Cursos.parquet, Dim_Modulos.parquet, etc.

---

> **Nota:** Según el enunciado, la arquitectura debe crearse en AWS S3, pero para esta práctica se ha representado aquí en formato textual.

