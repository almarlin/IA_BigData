import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits

# Cargar el dataset
digits = load_digits()

# Visualizar algunas imágenes
fig, axes = plt.subplots(2, 5, figsize=(10, 5))
for i, ax in enumerate(axes.flat):
    ax.imshow(digits.images[i], cmap="gray")
    ax.set_title(f"Dígito: {digits.target[i]}")
    ax.axis("off")

plt.show()

print(digits.data[0])  # Muestra los valores de los píxeles de la primera imagen

