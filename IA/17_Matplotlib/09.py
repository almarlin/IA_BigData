import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# El fichero “titanic.csv” contiene información sobre los pasajeros del Titanic. Crear
# un dataframe con Pandas y a partir del mismo, generar los siguientes diagramas;
# 1. Diagrama de Sectores con los fallecidos y supervivientes
# 2. Histograma con las edades
# 3. Diagrama de Barras con el número de personas en cada clase
# 4. Diagrama de Barras con el número de personas fallecidas y
# supervivientes en cada clase.
# 5. Diagrama de Barras con el número de personas fallecidas y
# supervivientes acumuladas en cada clase.

data = pd.read_csv("./ficheros/titanic.csv")

fig, diagrama = plt.subplots(3, 2)
# 1 --------------------
fallecidos = data[data["Survived"] == False]
supervivientes = data[data["Survived"] == True]

fallecidos_tot = fallecidos["Survived"].count()
supervivientes_tot = supervivientes["Survived"].count()
lista = [fallecidos_tot, supervivientes_tot]

diagrama[0, 0].set_title("Fallecidos/Supervivientes")
diagrama[0, 0].pie(lista, labels=["Fallecidos", "Supervivientes"], shadow=True)

# 2 --------------------
edades = data["Age"]
diagrama[0, 1].hist(edades)
diagrama[0, 1].set_title("Histograma de edades")

# 3 --------------------

divisionPorClase = data.groupby("Pclass")["PassengerId"].apply(list)
totales = []
for clase in divisionPorClase:
    totales.append(len(clase))

clases = divisionPorClase.keys()
diagrama[1, 0].bar(clases, totales)
diagrama[1, 0].set_title("Personas por clase")

# 4 --------------------


diagrama[1, 1].bar(
    (np.arange(len(clases)) + 1) - 0.4 / 2,
    supervivientes_tot,
    0.4,
    label="Supervivientes",
    color="orange",
)
diagrama[1, 1].bar(
    (np.arange(len(clases)) + 1) + 0.4 / 2,
    fallecidos_tot,
    0.4,
    label="Fallecidos",
    color="g",
)
diagrama[1, 1].legend()
diagrama[1, 1].set_title("Supervivientes y fallecidos por clase")


# 5 --------------------

diagrama[2, 0].bar(
    (np.arange(len(clases)) + 1),
    fallecidos_tot,
    0.4,
    bottom=supervivientes_tot,
    yerr=fallecidos_tot / 10,
    label="Fallecidos",
    color="g",
)
diagrama[2, 0].bar(
    (np.arange(len(clases)) + 1),
    supervivientes_tot,
    0.4,
    yerr=supervivientes_tot / 10,
    label="Supervivientes",
    color="orange",
)

diagrama[2, 0].legend()
diagrama[2, 0].set_title("Supervivientes y fallecidos por clase")
plt.tight_layout()
plt.show()
