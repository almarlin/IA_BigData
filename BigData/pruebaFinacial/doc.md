# Análisis Financiero
### Sistemas de Big Data
#### Alvaro Martínez Lineros

## 1. Exploración inicial del dataset.
Se ha realizado la carga del dataset en formato Dataframe de pandas para facilitar el manejo. Con los comandos `data.describe()` y `data.info()` podemos observar unas métricas básicas del dataframe, tipos de datos de las columnas, contador de valores nulos, tamaño y nombre de las columnas.

![informacionDatos](capturas/informacion.PNG)

## 2. Análisis descriptivo.
Con la información obtenida gracias al `data.describe()` podemos ver las métricas de cada columna.

Como valores a destacar de este primer análisis podemos ver como en algún momento no se obtuvieron beneficios, pues el mínimo es negativo `-40617.5000` y la desviación típica es `42760.626`. 

Los registros van de `2013-09-01` al `2014-12-01`, ese es el periodo de las ventas de este dataset.

## 3. Segmentación por categorías.
Si visualizamos los beneficios por los segmentos, podemos observar como en el segmento "Enterprise" se han tenido pérdidas y el segmento "Goverment" el que más beneficios ha tenido con diferencia.

![beneficios](capturas/beneficioSegmento.PNG)

## 4. Análisis por país.
El país con mayor volumen de ventas es Canadá con el 22% y el país con el menor volumen es Alemania con el 17.9%.

![ventas](capturas/ventasPaises.png)

## 5. Análisis temporal.
