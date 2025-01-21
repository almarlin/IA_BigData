import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Boxplot multivariado con ajuste de estilo

df = sns.load_dataset("diamonds")

carat = np.array(df["carat"])
price = np.array(df["price"])
depth = np.array(df["depth"])

rangos = [0, 0.3, 0.6, 1.0, 1.5, 2.0, 5.0]
titulos = ['0-0.3', '0.3-0.6', '0.6-1.0', '1.0-1.5', '1.5-2.0', '2.0-5.0']

carat_ranges = pd.cut(carat,bins=rangos,labels=titulos)

sns.boxplot(x=carat_ranges, y=price,hue=df["cut"],fill=False,gap=.3)
plt.xlabel("Quilates")
plt.ylabel("Precio")
plt.title("Precio del diamante por quilates y tipo de corte")
plt.show()
