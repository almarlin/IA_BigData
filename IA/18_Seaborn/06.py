import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Gráfico de barras con agregación de datos

df = sns.load_dataset("titanic")

clase = np.array(df["class"])
tarifa = np.array(df["fare"])

sns.barplot(x=clase,y=tarifa,hue=df["sex"],errorbar="sd")
plt.xlabel("Clase")
plt.ylabel("Tarifa")
plt.title("Tarifas por clase y género con desviación típica")
plt.show()
