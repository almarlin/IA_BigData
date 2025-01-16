import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Escribir una función que reciba una serie de Pandas con el número de ventas de un
# producto por años y una cadena con el tipo de gráfico a generar (líneas, barras,
# sectores, áreas) y devuelva un diagrama del tipo indicado con la evolución de las
# ventas por años y con el título “Evolución del Número de Ventas”.

ventas = pd.Series(np.random.randint(0,1000,10))
anyos = np.arange(2014,2024,1)

graficos = ["l","b","s","a"]

graf_sel = np.random.randint(0,4)
diagrama = plt.subplot()

if graficos[graf_sel] == "l":
    diagrama.plot(anyos,ventas,color="r")
    diagrama.set_title("Lineas")

elif graficos[graf_sel] == "b":
    diagrama.barh(anyos,ventas,color="g")
    diagrama.set_title("Barras")

elif graficos[graf_sel] == "s":
    explotar = np.zeros(10)
    explotar[pd.Series.idxmax(ventas)] = 0.2
    diagrama.pie(ventas,labels=anyos,explode=explotar)
    diagrama.set_title("Sectores")
    plt.legend(title="Años",bbox_to_anchor=(1.1,1))
    
elif graficos[graf_sel] == "a":
    diagrama.fill_between(anyos,ventas,color="gray")
    diagrama.set_title("Area")

plt.show()