import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd


df = sns.load_dataset("exercise")

duracion = df["time"]
tipo = df["kind"]

sns.catplot(
    x=tipo,
    y=duracion,
    kind="strip",
    order=["rest", "running", "walking"],
    jitter=True,
    height=6,
    aspect=1.5,
    hue=tipo,
    palette="Set1",
)

plt.title("Dispersión de Duración por Tipo de Ejercicio", fontsize=16)
plt.xlabel("Tipo de Ejercicio", fontsize=12)
plt.ylabel("Duración (minutos)", fontsize=12)
plt.show()
