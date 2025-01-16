import matplotlib.pyplot as plt
import numpy as np

# Escribir una función que reciba un diccionario con las notas de las asignaturas de
# un curso y una cadena con el nombre de un color y devuelva un diagrama de barras
# de las notas en el color dado.

curso = {
    "Matemáticas": np.random.randint(0,11),
    "Lengua": np.random.randint(0,11),
    "Historia": np.random.randint(0,11),
    "Inglés": np.random.randint(0,11),
    "Programación": np.random.randint(0,11),
    "Química": np.random.randint(0,11),
}

colores = [
    "b",  # Azul
    "g",  # Verde
    "r",  # Rojo
    "c",  # Cyan
    "m",  # Magenta
    "y",  # Amarillo
    "k",  # Negro
    "orange",  # Naranja
    "purple",  # Púrpura
]

asignaturas = list(curso.keys())
notas = list(curso.values())

color_sel = colores[np.random.randint(0, 9)]
diagrama = plt.subplot()
diagrama.set_title("Notas")
diagrama.axhline(y=5,color="grey",linestyle="--",label="Aprobado")
plt.legend()
plt.xlabel("Asignaturas")
plt.ylabel("Media de asignatura")
diagrama.bar(asignaturas,notas,color=color_sel)
plt.show()