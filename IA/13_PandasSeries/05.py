import pandas as pd
import numpy as np

productos = ["Producto A", "Producto B", "Producto C", "Producto D", "Producto E", "Producto F", "Producto G", "Producto H"]
stock = []

print("Introduce la cantidad en stock de 8 productos diferentes:")

for producto in productos:
    cantidad = input(f"{producto}: ")
    try:
        stock.append(int(cantidad))
    except ValueError:
        stock.append(np.nan)

stock_serie = pd.Series(stock, index=productos)

productos_menos_10 = stock_serie[stock_serie < 10].dropna()

stock_serie_rellena = stock_serie.fillna(0)

stock_ordenado = stock_serie_rellena.sort_values()

print("\nProductos con menos de 10 unidades:")
print(productos_menos_10)

print("\nProductos con valores faltantes rellenados con 0:")
print(stock_serie_rellena)

print("\nProductos ordenados por la cantidad en stock:")
print(stock_ordenado)
