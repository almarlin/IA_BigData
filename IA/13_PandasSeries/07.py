import pandas as pd
import matplotlib.pyplot as plt

tiendas = ["A", "B", "C", "D", "E"]
data = []

for t in tiendas:
    data.append(float(input(f"Introduce el precio en la tienda {t}\n")))
    
precios = pd.Series(data,tiendas)

print(f"Precio más alto: {precios.max()} en la tienda {precios.idxmax()}")
print(f"Precio más bajo: {precios.min()} en la tienda {precios.idxmin()}")

precios_encima_mediana = precios[precios > precios.median()]
print(f"Precios por encima de la mediana\n{precios_encima_mediana}")

precios = precios.fillna(precios.mean())

plt.figure(figsize=(8, 6))
precios.plot(kind="bar", color="skyblue")
plt.title("Precios del Producto en Diferentes Tiendas")
plt.xlabel("Tienda")
plt.ylabel("Precio")
plt.xticks(rotation=0)
plt.grid(axis="y")
plt.show()