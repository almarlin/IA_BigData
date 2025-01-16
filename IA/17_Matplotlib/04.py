import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Escribir una función que reciba una serie de Pandas con las notas de los alumnos
# de un curso y devuelva un diagrama de cajas con las notas. El diagrama debe tener
# el título “Distribución de Notas”.

notas = pd.Series(np.random.randint(0,11,30))

diagrama = plt.subplot()
diagrama.boxplot(notas,medianprops=dict(color='orange', linewidth=2))
diagrama.set_title("Distribución de notas")
plt.axhline(5, color='gray', linestyle='--', label='Aprobado')
plt.legend()
plt.xlabel("Grupo de alumnos")
plt.ylabel("Notas")
plt.show()
