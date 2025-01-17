import seaborn as sns
import matplotlib.pyplot as plt

# Basada sobre matplotlib, libreria para graficos estadisticos.
# Se vera con profundidad en Big Data.
#
# Es necesario utilizarlo con matplotlib

# Listar datasets disponibles (de ejemplo)
print(sns.get_dataset_names())

# Cargar dataset de ejemplo
propinas = sns.load_dataset("tips")
pingus = sns.load_dataset("penguins")
titanic = sns.load_dataset("titanic")

# Mostrar un dataset

sns.scatterplot(propinas,x="total_bill",y="tip",hue="sex")
plt.show()