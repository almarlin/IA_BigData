import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Regresión lineal múltiple con visualización avanzada

df = sns.load_dataset("mpg")

horsepower = df["horsepower"]
weight = df["weight"]

sns.lmplot(data=df,x="horsepower",y="weight",ci=95,line_kws={"color":"green"})

plt.title("Relación entre Peso y Potencia con Intervalo de Confianza del 95%", fontsize=16)
plt.xlabel("Peso (lbs)", fontsize=12)
plt.ylabel("Potencia (horsepower)", fontsize=12)
plt.tight_layout()
plt.show()