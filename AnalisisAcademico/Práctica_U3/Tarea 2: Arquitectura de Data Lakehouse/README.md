# Arquitectura Medallón (Bronce – Plata – Oro)
Proyecto: Análisis Académico

Este documento define la arquitectura en capas del Data Lakehouse para el proyecto de análisis académico, siguiendo el modelo Medallón recomendado por Databricks (Bronce → Plata → Oro).  
Aunque el enunciado indica implementarlo en AWS S3, en esta práctica se describe en formato textual para facilitar la entrega.

---

## 🟫 Capa Bronce (Raw Layer)
**Descripción:**  
Contiene los datos académicos tal y como se exportan desde ÍTACA y las actas oficiales.  
Es una capa inmutable, sin limpieza y sin transformaciones.

**Características:**
- Formato original (CSV).
- Puede contener errores, duplicados, nulos o valores fuera de rango.
- Se actualiza 3 veces al año (tras cada evaluación).
- Contiene históricos de cursos anteriores.

**Ejemplos de ficheros:**
- `alumnos_raw.csv`
- `calificaciones_raw.csv`
- `cursos_raw.csv`
- `modulos_raw.csv`
- `grupos_raw.csv`

**Ubicación lógica (AWS S3):**

