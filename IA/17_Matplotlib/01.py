import matplotlib.pyplot as plt
import math
import numpy as np

# Utilizar la función de la raíz cuadrada (librería Math), generar un gráfico (Matplotlib)
# de dispersión (Random) en el que se muestre 20 números enteros aleatorios entre
# el 0 y 100 en el eje X y su raíz cuadrada en el eje Y.

nums = np.random.randint(0,100,20)
sqrt = [math.sqrt(num) for num in nums]

diagrama = plt.subplot()
diagrama.scatter(nums,sqrt)
diagrama.set_title("Diagrama de dispersión")
plt.xlabel("Números random")
plt.ylabel("Raíz cuadrada")
plt.show()
