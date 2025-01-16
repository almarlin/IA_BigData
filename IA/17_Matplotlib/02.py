import matplotlib.pyplot as plt
import numpy as np

# Escribir un programa que pregunte al usuario por las ventas de un rango de años y
# muestre por pantalla un diagrama de líneas con la evolución de las ventas.

years = np.arange(2014, 2025, 1)
sales = []
for year in years:
    while True:
        try:
            data = float(input(f"¿Cuáles fueron tus ventas en el año {year}? "))
            # data = np.random.randint(1,1000)
            sales.append(data)
            break
        except ValueError:
            print("Por favor ingresa un número válido.")

diagram = plt.subplot()
diagram.plot(years, sales, linestyle="dashed",color="r")
diagram.set_title("Ventas/Año")
plt.xlabel("Años")
plt.ylabel("Ventas realizadas")
plt.show()
