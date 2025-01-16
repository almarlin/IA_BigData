import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Escribir una función que reciba un dataframe de Pandas con los ingresos y gastos
# de una empresa por meses y devuelva un diagrama de líneas con dos líneas, la
# primera para los ingresos, y la segunda para los gastos. El diagrama debe tener una
# leyenda identificando la línea de los ingresos y la de los gastos, un título con el
# nombre “Evolución de Ingresos y Gastos” y el eje Y debe empezar en 0.

meses = [
    "Enero",
    "Febrero",
    "Marzo",
    "Abril",
    "Mayo",
    "Junio",
    "Julio",
    "Agosto",
    "Septiembre",
    "Octubre",
    "Noviembre",
    "Diciembre",
]
ingresos = np.random.randint(0, 10000, 12)
gastos = np.random.randint(0, 10000, 12)

data = {"Mes": meses, "Ingresos": ingresos, "Gastos": gastos}
ingresosGastos = pd.DataFrame(data)

diagrama = plt.subplot()
diagrama.plot(ingresosGastos["Mes"], ingresosGastos["Ingresos"], label="Ingresos")
diagrama.plot(ingresosGastos["Mes"], ingresosGastos["Gastos"], label="Gastos")
plt.xticks(rotation=35, ha="right")
plt.legend()
diagrama.set_title("Evolución de ingresos y gastos")

plt.show()
