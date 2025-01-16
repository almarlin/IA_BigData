import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Escribir una función que reciba una serie de Pandas con el número de ventas de un
# producto durante los meses de un trimestre y un título, y cree un diagrama de
# sectores con las ventas en formato PNG con el título dado. El diagrama debe
# guardarse en un fichero con el formato PNG y el título dado.

ventas = pd.Series(np.random.randint(0,1000,3))
meses = ["Enero","Febrero","Marzo"]
titulo = "Ventas de relojes Enero-Abril"

explotar = [0,0,0]
explotar[pd.Series.idxmax(ventas)] = 0.2

diagrama = plt.subplot()
diagrama.pie(ventas,labels=meses,shadow=True,explode=explotar)
diagrama.set_title(titulo)
plt.legend()
plt.savefig("./graficos/05.png")
plt.show()


