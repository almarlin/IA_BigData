import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = sns.load_dataset("iris")

sepal_length = np.array(df["sepal_length"])
species = np.array(df["species"])

sns.violinplot(x=species,y=sepal_length,inner="point")
plt.xlabel("Especies")
plt.ylabel("Longitud del sépalo")
plt.title('Distribución de la Longitud del Sépalo por Especie')
plt.show()