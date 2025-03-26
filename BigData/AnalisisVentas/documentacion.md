# DAX aplicado al análisis de ventas
### Sistemas de Big Data
#### Alvaro Martínez Lineros

## 1. Análisis General de Ventas (AV)
```
1_AV_Total_Ventas = SUM(retail_sales_dataset[Total Amount])
------------------------------------------------------------------------------------------------
2_AV_Total_transacciones = COUNT(retail_sales_dataset[Customer ID])
------------------------------------------------------------------------------------------------
3_AV_Promedio_Ventas = AVERAGE(retail_sales_dataset[Total Amount])
------------------------------------------------------------------------------------------------
4_AV_Clientes_Unicos = DISTINCTCOUNT(retail_sales_dataset[Customer ID])
------------------------------------------------------------------------------------------------
5_AV_Total_Productos_Vendidos = SUM(retail_sales_dataset[Items Purchased])
------------------------------------------------------------------------------------------------
6_AV_Promedio_Diario = AVERAGEX(VALUES(retail_sales_dataset[Date]),CALCULATE(AVERAGE(retail_sales_dataset[Total Amount])))
------------------------------------------------------------------------------------------------
7_AV_Total_Ventas_Categoria = SUMX(VALUES(retail_sales_dataset[Product Category]),SUM(retail_sales_dataset[Total Amount]))
------------------------------------------------------------------------------------------------
8_AV_Producto_Mas_Vendido = 
CALCULATE(
    FIRSTNONBLANK(retail_sales_dataset[Product], 1),
    TOPN(
        1, 
        SUMMARIZE(
            retail_sales_dataset, 
            retail_sales_dataset[Product], 
            "TotalQuantity", SUM(retail_sales_dataset[Quantity])
        ),
        [TotalQuantity], 
        DESC
    )
)
------------------------------------------------------------------------------------------------
9_AV_AVG_Carrito = AVERAGE(retail_sales_dataset[Total Amount])
------------------------------------------------------------------------------------------------
10_AV_Dia_Mayor_Volumen = 
VAR DiaMaxVentas = 
    TOPN(
        1, 
        VALUES(retail_sales_dataset[Date]), 
        CALCULATE( COUNT(retail_sales_dataset[Transaction ID]) ), 
        DESC
    )
// Funciona tanto MINX como MAXX pues DiaMaxVentas es una tabla con un solo registro. 
// Se selecciona la fecha minima (retail_sales_dataset[Date]) de la tabla DiaMaxVentas 
RETURN MINX(DiaMaxVentas,retail_sales_dataset[Date])
------------------------------------------------------------------------------------------------
```
## 2. Análisis de Clientes y Comportamiento de Compra (AC)
```
1_AC_Clientes_Recurrentes = CALCULATE(
    DISTINCTCOUNT(retail_sales_dataset[Customer ID]),
    FILTER(
        VALUES(retail_sales_dataset[Customer ID]),
        CALCULATE(COUNT(retail_sales_dataset[Transaction ID]))> 1
    )
)
------------------------------------------------------------------------------------------------
2_AC_Promedio_Cliente = AVERAGEX(
    VALUES(retail_sales_dataset[Customer ID]),
    CALCULATE(SUM(retail_sales_dataset[Total Amount]))
)
------------------------------------------------------------------------------------------------
3_AC_Cliente_Mayor_Gasto = 
        CALCULATE(
        FIRSTNONBLANK(retail_sales_dataset[Customer ID], 1),
        FILTER(
            retail_sales_dataset,
            retail_sales_dataset[Total Spend] = 
                MAXX(
                    ALL(retail_sales_dataset),
                    retail_sales_dataset[Total Spend]
                )
        )
)
------------------------------------------------------------------------------------------------
4_AC_Clientes_solo_1_vez = CALCULATE(
    DISTINCTCOUNT(retail_sales_dataset[Customer ID]),
    FILTER(
        VALUES(retail_sales_dataset[Customer ID]),
        CALCULATE(COUNT(retail_sales_dataset[Transaction ID])) == 1
    )
)
------------------------------------------------------------------------------------------------
5_AC_Promedio_productos_por_cliente = AVERAGEX(
    VALUES(retail_sales_dataset[Customer ID]),
    CALCULATE(SUM(retail_sales_dataset[Quantity]))
)
------------------------------------------------------------------------------------------------
6_AC_Frecuencia_Promedio = AVERAGE(retail_sales_dataset[Days Since Last Purchase])
------------------------------------------------------------------------------------------------
7_AC_Ciudad_Mas_Compras = 
    VAR ciudadTop = 
        TOPN(
            1,
            SUMMARIZE(
                retail_sales_dataset,
                retail_sales_dataset[City],
                "ciudad",COUNTROWS(retail_sales_dataset)
            ),
            [ciudad],
            DESC
        )
    return MAXX(ciudadTop,retail_sales_dataset[City])
------------------------------------------------------------------------------------------------
8_AC_Tasa de conversion = (No hay visitas a productos)
------------------------------------------------------------------------------------------------
9_AC_Categoria_max_clientes_unicos = 
CALCULATE(
    FIRSTNONBLANK(retail_sales_dataset[Product Category],1),
    FILTER(
        VALUES(retail_sales_dataset[Product Category]),
        CALCULATE(DISTINCTCOUNT(retail_sales_dataset[Customer ID])) =
        MAXX(
            VALUES(retail_sales_dataset[Product Category]),
            CALCULATE(DISTINCTCOUNT(retail_sales_dataset[Customer ID]))
        )   
    )
)
------------------------------------------------------------------------------------------------
10_AC_Carritos_Abandonados = CALCULATE(
    COUNTROWS(retail_sales_dataset),retail_sales_dataset[Total Amount] = 0
)
------------------------------------------------------------------------------------------------
```
## 3. Análisis de Productos (AP)
```
1_AP_Productos_No_Vendidos = 
EXCEPT( 
    ALL(retail_sales_dataset[Product]), 
    VALUES(retail_sales_dataset[Product]) 
)
------------------------------------------------------------------------------------------------
2_AP_Promedio_Vendidos = 
AVERAGEX(
    VALUES(retail_sales_dataset[Product]),
    CALCULATE(AVERAGE(retail_sales_dataset[Price per Unit]))
)
------------------------------------------------------------------------------------------------
3_AP_Producto_Mayor_Ganancia = CALCULATE(
    FIRSTNONBLANK(VALUES(retail_sales_dataset[Product]),1),
    FILTER(
            retail_sales_dataset,
            retail_sales_dataset[Total Amount] = 
                MAXX(
                    ALL(retail_sales_dataset),
                    retail_sales_dataset[Total Amount]
                )
    )
)
------------------------------------------------------------------------------------------------
4_AP_Promedio_por_producto = AVERAGEX(
    VALUES(retail_sales_dataset[Product]), 
    CALCULATE(COUNT(retail_sales_dataset[Transaction ID]))
)
------------------------------------------------------------------------------------------------
5_AP_Productos_Mas_Juntos = [No se incluyen listas de productos comprados juntos]
------------------------------------------------------------------------------------------------
6_AP_Devoluciones = [No se incluyen devoluciones]
------------------------------------------------------------------------------------------------
7_AP_Stock_Promedio = AVERAGE(retail_sales_dataset[Stock])
------------------------------------------------------------------------------------------------
8_AP_Producto_Mayor_Variacion = 
VAR Producto = 
    TOPN(
        1, 
        SUMMARIZE(
            retail_sales_dataset, 
            retail_sales_dataset[Product], 
            "Variacion", 
            [VariacionPrecio]
        ), 
        [VariacionPrecio], 
        DESC
    )
RETURN
    FIRSTNONBLANK(SELECTCOLUMNS(Producto, "Product", retail_sales_dataset[Product]), 1)
------------------------------------------------------------------------------------------------
9_AP_Productos_por_Categoria = COUNTROWS(
    VALUES(retail_sales_dataset[Product])
)
------------------------------------------------------------------------------------------------
10_AP_Producto_Mayor_Descuento = [No se indica la cantidad de descuento aplicado al producto]
------------------------------------------------------------------------------------------------
```
## 4. Análisis Temporal (AT)
```
1_AT_Total_Ventas_Mes = CALCULATE(
     SUM(retail_sales_dataset[Total Amount]),
        DATESMTD(retail_sales_dataset[Date])
)
------------------------------------------------------------------------------------------------
2_AT_Dia_Semana_Mas_Ventas = 
VAR diaMaxVentas =
    TOPN(
        1,
        VALUES(retail_sales_dataset[diaSemana]),
        CALCULATE(SUM(retail_sales_dataset[Total Amount])),
        DESC
    )
RETURN MINX(diaMaxVentas,retail_sales_dataset[diaSemana])
------------------------------------------------------------------------------------------------
3_AT_Crecimiento_por_Mes = CALCULATE(
    COUNT(retail_sales_dataset[Transaction ID]),
    MONTH(retail_sales_dataset[Date])
)
------------------------------------------------------------------------------------------------
4_AT_Hora_Mas_Transacciones = CALCULATE(
    CALCULATE(
        FIRSTNONBLANK(retail_sales_dataset[Date], 1),
        FILTER(
            retail_sales_dataset,
            retail_sales_dataset[Total Amount] = 
                MAXX(
                    ALL(retail_sales_dataset),
                    retail_sales_dataset[Total Amount]
                )
        )
    )
)
------------------------------------------------------------------------------------------------
5_AT_Temporada_mas_ventas = 
VAR temporada = 
    TOPN( 
        1, 
        SUMMARIZE(
            retail_sales_dataset,
            retail_sales_dataset[Date].[Trimestre],
            "Ventas",SUM(retail_sales_dataset[Total Amount])
        ),
        [Ventas],
        DESC
    )
RETURN MINX(temporada,retail_sales_dataset[Date].[Trimestre])
------------------------------------------------------------------------------------------------
6_AT_Diferencia_laboral_finde = 
VAR laboral = 
    CALCULATE(
        SUM(retail_sales_dataset[Total Amount]),
        retail_sales_dataset[tipoDia] = "Laborable"
    )
VAR finde = 
    CALCULATE(
        SUM(retail_sales_dataset[Total Amount]),
        retail_sales_dataset[tipoDia] = "Fin de Semana"
    )
RETURN 
    laboral - finde
------------------------------------------------------------------------------------------------
7_AT_Crecimiento_Mensual = CALCULATE(
    SUM(retail_sales_dataset[Total Amount]),
    MONTH(retail_sales_dataset[Date])
)
------------------------------------------------------------------------------------------------
9_AT_Promedio_Ventas_por_Dia = 
AVERAGEX(
    VALUES(retail_sales_dataset[diaSemana]),
    CALCULATE(SUM(retail_sales_dataset[Total Amount]))
)
------------------------------------------------------------------------------------------------
10_AT_Tendencia_Estacional = 
VAR temporada = 
TOPN( 5, SUMMARIZE(retail_sales_dataset,
retail_sales_dataset[Date].[Trimestre],
"Ventas",[Ventas_por_temporada]),
[Ventas_por_temporada],
DESC)
RETURN FIRSTNONBLANK(SELECTCOLUMNS(temporada,"Trimestre",retail_sales_dataset[Date].[Trimestre]),5)
------------------------------------------------------------------------------------------------
```
## 5. Análisis Logístico y de Inventario (ALI)
```
1_ALI_Tot_prod_stock = 
CALCULATE(
    DISTINCTCOUNT(retail_sales_dataset[Product]),
    retail_sales_dataset[Stock] > 0
)
------------------------------------------------------------------------------------------------
2_ALI_Prod_menor_stock = 
TOPN(
    5,
    SUMMARIZE(
        retail_sales_dataset,
        retail_sales_dataset[Product],
        "StockTotal", SUM(retail_sales_dataset[Stock])
    ),
    [StockTotal],
    ASC
)
------------------------------------------------------------------------------------------------
3_ALI = []
------------------------------------------------------------------------------------------------
4_ALI = [No hay fecha de reposición de productos]
------------------------------------------------------------------------------------------------
5_ALI = [No hay fecha de entrega]
------------------------------------------------------------------------------------------------
6_ALI = [No hay fecha de entrega ni fecha de entrega prevista]
------------------------------------------------------------------------------------------------
7_ALI_Productos_Agotados = 
CALCULATE(
    DISTINCTCOUNT(retail_sales_dataset[Product]),
    retail_sales_dataset[Stock] = 0,
    retail_sales_dataset[Date] >= retail_sales_dataset[Date] - 30
)
------------------------------------------------------------------------------------------------
8_ALI_Categorias_Menos_Stock = 
TOPN( 
    1, 
    VALUES(retail_sales_dataset[Product Category]), 
    CALCULATE( SUM(retail_sales_dataset[Stock]) ), 
    ASC 
)
------------------------------------------------------------------------------------------------
9_ALI_Comparacion_Demanda_Historica = 
// Cogemos la fecha más actual del producto a comparar su demanda
VAR fechaMax = 
CALCULATE(
    MAX(retail_sales_dataset[Date]),
    retail_sales_dataset[Product] = "Samsung Galaxy S21 Ultra"
)
// Establecemos una fecha límite
VAR FechaLimite = fechaMax - 90
// Calculamos la demanda promedio con AVG filtrando por producto y fecha
VAR DemandaPromedio = 
    CALCULATE(
        AVERAGE( retail_sales_dataset[Quantity] ),  
        retail_sales_dataset[Product] = "Samsung Galaxy S21 Ultra",
        retail_sales_dataset[Date] >= FechaLimite
    )
// Recogemos el stock actual con MAX filtrando por producto y fecha
VAR StockActual = 
    CALCULATE(
        MAX( retail_sales_dataset[Stock] ),  
        retail_sales_dataset[Product] = "Samsung Galaxy S21 Ultra",
        retail_sales_dataset[Date] = fechaMax
    )
// Calculamos la cobertura de días dividiendo el stock entre la demanda diaria promedio
VAR CoberturaDias = 
    IF(DemandaPromedio > 0, StockActual / DemandaPromedio, BLANK())
// La demanda futura será 30 veces (días) la demanda promedio
VAR DemandaFutura = DemandaPromedio * 30
// Finalmente la cantidad a reponer será la diferencia de la demanda futura con el stock actual
VAR CantidadReponer = MAX(0, DemandaFutura - StockActual)

RETURN 
IF(
    ISBLANK(CoberturaDias), 
    BLANK(), 
    "Cobertura: " & FORMAT(CoberturaDias, "0.0") & " días | Reponer: " & FORMAT(CantidadReponer, "0") 
)
------------------------------------------------------------------------------------------------
10_ALI = [No hay pedidos de reposición de inventario]
------------------------------------------------------------------------------------------------
```
## 6. Análisis Complejo y Predictivo (ACP) -- Extra + 1 punto

```
------------------------------------------------------------------------------------------------
2_ACP_Prediccion_Ventas = 
// Creamos la tabla datos. 
    VAR datos =
        ADDCOLUMNS(
            // Agrupamos por año y mes y agregamos las columnas X e Y a la tabla datos
            SUMMARIZE(
                retail_sales_dataset,
                retail_sales_dataset[Date].[Año],
                retail_sales_dataset[NumMes]
            ),
            // Transforma año y mes a un único numero (en meses)
            "X", retail_sales_dataset[Date].[Año] * 12 + retail_sales_dataset[NumMes],
            // El total de ventas de ese mes
            "Y", CALCULATE(SUM(retail_sales_dataset[Total Amount]))
        )
    // Calcula la regresión lineal de las ventas respecto a los meses
    VAR regresion = LINESTX(datos, [Y], [X])  

    // Recogemos la pendiente y la interseccion de la tabla que devuelve la regresion
    VAR pendiente = SELECTCOLUMNS(regresion, "Slope", [Slope1])
    VAR interseccion = SELECTCOLUMNS(regresion, "Intercept", [Intercept])

    // Encuentra el mes mas reciente de los datos
    VAR ultimoX = MAXX(datos, [X])

    // Predecimos las ventas del proximo mes aplicando la pendiente y sumando la interseccion
    RETURN pendiente * (ultimoX + 1) + interseccion
------------------------------------------------------------------------------------------------
```