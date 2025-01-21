import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

df = sns.load_dataset("penguins")

# Eliminar filas con valores NaN porque dan problemas
df_clean = df.dropna(subset=["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"])

bill_length = df_clean["bill_length_mm"]
bill_depth = df_clean["bill_depth_mm"]
flipper_length = df_clean["flipper_length_mm"]
body_mass = df_clean["body_mass_g"]

matriz = np.column_stack((bill_depth, bill_length, flipper_length, body_mass))

correlacion = np.corrcoef(matriz, rowvar=False)  # rowvar=False hace que las columnas sean las variables

sns.heatmap(correlacion, annot=True, cmap="coolwarm", fmt=".2f", xticklabels=["Bill Depth", "Bill Length", "Flipper Length", "Body Mass"], yticklabels=["Bill Depth", "Bill Length", "Flipper Length", "Body Mass"])

plt.title("Matriz de Correlación de las Características de los Pingüinos")
plt.show()
