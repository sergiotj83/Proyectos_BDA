-Análisis Académico - Tarea 1: La Primera Inspección 

Conviértete en un detective y responde a estas preguntas para cada fichero: 

1-¿Cuál es el separador de columnas (coma , o punto y coma ; )? 

2-¿La primera fila contiene los nombres de las columnas (encabezados)? ¿Son claros? 

3-Inspecciona visualmente las primeras 20-30 filas. ¿Ves valores que te parezcan extraños o que faltan (celdas vacías, "N/A", "s/d")? 

4- ¿Los formatos son consistentes? Por ejemplo, ¿las fechas están siempre como DD/MM/AAAA o a veces cambian? 

5-Identifica las "claves" o "IDs" que podrían servir para relacionar unos ficheros con otros (ej: id_alumno en el fichero de calificaciones.csv y también en alumnos.csv). 

 

Análisis de INDICADORES. 

· Indicadores_Finales. 

1-El uso de “;” es correcto, porque los valores numéricos usan coma decimal, lo que evitaría conflictos si se hubiera usado “,” como separador. 

2-Los encabezados están bien definidos, pero en el uso de abreviaturas habría que consultar al cliente su significado para evitar interpretaciones erróneas.  

3- Los campos de Valor-T1,T2 y T3 presentan ausencia de datos que puede ser un indicador de que no todos los Indicadores se midan trimestralmente, y en este caso son anuales. 

Si filtramos Periodicidad por trimestral tenemos valores para Cod_SQ pero PAA está siempre en blanco en cambio, si filtramos y marcamos anual se dan todos los casos posibles, que solo aparezca SQ solo PAA, ninguno o ambos.4 

-En la columna Escala, se mezclan datos numéricos y de texto (Anual), igual que en las columnas Cod_SQ y Cod_PAA 

5-La PK de esta tabla está compuesta por Curso e Identificador, ya que su combinación genera un Indicador único con sus respectivos valores y no nulos. 



·Procesos 

1-Este archivo usa “,” como separador. Esto en primer lugar refleja falta de homogeneidad en el conjunto de archivos, pero analizando el archivo en sí, no supondría un problema ya que no hay datos numéricos. 

2-Los encabezados están bien definidos y sin abreviaturas. 

3-No se detectan valores nulos ni inconsistencias. 

4-Los datos mostrados son homogéneos.  

5-La clave primaria de esta tabla es Proceso, ya que es un campo que genera valores únicos y no nulos. 

 

·Lineas 

1-Este archivo usa “,” como separador, esto en primer lugar refleja falta de homogeneidad en el conjunto de archivos, pero analizando el archivo en sí, no supondría un problema ya que no hay datos numéricos. 

2-Los encabezados están bien definidos, y no hay abreviaturas que puedan generar confusión. 

3-No se detectan valores nulos ni inconsistencias. 

4-Los datos mostrados son homogéneos.  

5-La clave primaria de esta tabla es Linea ya que genera valores únicos de Descripción_Linea y no nulos. 

 
 

·Objetivos 

1-Este archivo usa “,” como separador, esto en primer lugar refleja falta de homogeneidad en el conjunto de archivos, pero analizando el archivo en sí, no supondría un problema ya que no hay datos numéricos. 

2-Los encabezados están bien definidos. Hay abreviaturas que, aunque puedan resultar fácilmente interpretables, habría que confirmar con el cliente su significado. 

3-No se detectan valores nulos ni inconsistencias. 

4-Los datos mostrados son homogéneos.  

5- En esta tabla el Objetivo_PAA es la clave primaria ya que genera valores únicos. Vemos que Descripción_Objetivo también son valores únicos, pero no se puede considerar la clave primaria ya que tiene un valor más causa/efecto. Es decir, tenemos el objetivo y su explicación, pero el dato importante es el objetivo en si. 

 

·Relaciones 

Indicadores-Procesos.(1:N) 

Por una parte, tenemos la relación de la que sería la tabla principal Indicadores con Procesos mediante sus claves Identificador y Proceso respectivamente. Analizando la primera línea de Indicadores: 

IPC01.01  
	

Satisfacció del professorat amb la gestió d’horaris [4]  
Vemos una relación conceptual de dichos campos, de forma que el anterior se incluye dentro de: 
PC01 
	
Organització delcurs acadèmic 

Indicadores-Objetivos-Lineas (1:N//1:N) 

Por otra parte, tenemos la relación conceptual entre estas tablas, de forma que en cada Identificador de Indicadores tenemos unas Lineas que se desglosan en diferentes Objetivos. 

 

 


Análisis de DATOS. 

1-Todos los archivos usan “,”, lo que aporta homogeneidad al proyecto, pero no alcanzo a valorar si podría llegar a ser un problema; ya que hay datos numéricos, pero como dígitos identificativos de tipo entero y no con decimales. 

 

·Alumnos 

2-Los encabezados están bien definidos. Hay abreviaturas que, aunque puedan resultar fácilmente interpretables, habría que confirmar con el cliente su significado. 

3-Hay columnas que están vacías como dictamen y fecha_resolución y otras con muchos campos vacíos y/o repetidos. 

4-Los datos mostrados son homogéneos.  

5- En esta tabla el NIA es la clave primaria. 

 

·Calificaciones. 

2-Los encabezados están bien definidos y sin abreviaturas. 

3-Hay columnas que están vacías como bloque_contenido, capacidades_inf, y medidas_inf.  

La columna observación aparentemente vacía, tiene datos en algunos campos. Esto podría dar lugar a confusión si llegase a ser un campo importante para el desarrollo del proyecto. 

4-Los datos en la columna evaluación mezcla formato numérico y de texto. 

5- En esta tabla, la clave primaria es la resultante de filtrar por alumno, evaluación y contenido. 

 

·Cursos 

2-Los encabezados están bien definidos y las dos abreviaturas son claras. 

3-No se aprecia ningún valor extraño. 

4-La columna abreviatura mezcla datos de tipo numérico y texto. 

5-La clave primaria es codigo. 



·Grupos  

2-Los encabezados están bien definidos. 

3-No se aprecia ningún valor extraño. Las columnas ensenanza, linea y oficial, muestran un único valor repetido. 

4-Los datos mostrados son homogéneos. 

5-La clave primaria es codigo. 

 

·Horas 

2-Los encabezados están bien definidos y sin abreviaturas. 

3-No se aprecia ningún valor extraño. 

4-La columna codigo, muestra valores numéricos y de texto. 

5-La clave primaria es la compuesta por codigo y ciclo, lo cual tiene sentido conceptual ya que una asignatura puede impartirse en varios ciclos, pero será única en el ciclo. 

 

·Modulos 

2-Los encabezados están bien definidos y las dos abreviaturas son entendibles. 

3-No se aprecia ningún valor extraño. 

4- La columna codigo, muestra valores numéricos y de texto. 

5-La clave primaria es la compuesta por codigo y curso. Conceptualmente igual que en la tabla horas, y esto nos permite ver que son tablas que manejan información muy similar. 

 


·Relaciones 

Alumnos-Calificaciones 1:N 

Cursos-Calificaciones 1:N 

Cursos-Modulos 1:N 

Modulos-Horas 1:N 
