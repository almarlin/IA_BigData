import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Histogramas superpuestos con diferentes bins


# Número de muestras y columnas
n_samples = 100
n_columns = 5
# Simulamos distribuciones normales
# data = np.random.normal(loc=0, scale=1, size=(n_samples, n_columns))
data1 = np.random.normal(loc=0, scale=1, size=(n_samples, 1))
data2 = np.random.normal(loc=1, scale=1.25, size=(n_samples, 1))
data3 = np.random.normal(loc=2, scale=0.5, size=(n_samples, 1))
data4 = np.random.normal(loc=3, scale=1.5, size=(n_samples, 1))
data5 = np.random.normal(loc=4, scale=2, size=(n_samples, 1))

data = np.concatenate((data1,data2,data3,data4,data5),axis=1)


# Creamos el DataFrame
df = pd.DataFrame(data, columns=[f'columna_{i+1}' for i in range(n_columns)])

columna_1=df["columna_1"]
columna_2=df["columna_2"]
columna_3=df["columna_3"]
columna_4=df["columna_4"]
columna_5=df["columna_5"]

sns.histplot(data,bins=20,kde=True,element="step",stat="density")
plt.title("Histograma con distribuciones normales superpuestas.")
plt.show()