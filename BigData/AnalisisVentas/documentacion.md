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
10_AV_Dia_Mayor_Volumen = CALCULATE(
        FIRSTNONBLANK(retail_sales_dataset[Date], 1),
        FILTER(
            ALL(retail_sales_dataset),
            COUNT(retail_sales_dataset[Transaction ID]) = 
                MAXX(
                    ALL(retail_sales_dataset[Date]),
                    COUNT(retail_sales_dataset[Transaction ID])
                )
        )
)
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
CALCULATE(
    FIRSTNONBLANK(retail_sales_dataset[City],1),
    FILTER(
        VALUES(retail_sales_dataset[City]),
        CALCULATE(SUM(retail_sales_dataset[Total Amount])) = 
        MAXX(VALUES(retail_sales_dataset[City]), CALCULATE(SUM(retail_sales_dataset[Total Amount])))
    )
)
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
1_AP_Productos_No_Vendidos = FILTER(
        ALL(retail_sales_dataset[Product]),
        NOT(
            retail_sales_dataset[Product] IN 
            VALUES(retail_sales_dataset[Product])
        )
)
------------------------------------------------------------------------------------------------
2_AP_Promedio_Vendidos = AVERAGEX(
    VALUES(retail_sales_dataset[Product]),
    CALCULATE(sum(retail_sales_dataset[Price per Unit]))
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
5_AP_Productos_Mas_Juntos = (No se incluyen listas de productos comprados juntos)
------------------------------------------------------------------------------------------------
6_AP_Devoluciones = (No se incluyen devoluciones)
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
10_AP_Producto_Mayor_Descuento = (No se indica la cantidad de descuento aplicado al producto)
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
TOPN( 1, SUMMARIZE(retail_sales_dataset,
retail_sales_dataset[Date].[Trimestre],
"Ventas",[Ventas_por_temporada]),
[Ventas_por_temporada],
DESC)
RETURN FIRSTNONBLANK(SELECTCOLUMNS(temporada,"Trimestre",retail_sales_dataset[Date].[Trimestre]),1)
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

------------------------------------------------------------------------------------------------

------------------------------------------------------------------------------------------------

------------------------------------------------------------------------------------------------

------------------------------------------------------------------------------------------------

------------------------------------------------------------------------------------------------

------------------------------------------------------------------------------------------------

------------------------------------------------------------------------------------------------

------------------------------------------------------------------------------------------------
```