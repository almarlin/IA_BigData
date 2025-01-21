import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Gráfico de dispersión avanzado con estilo personalizado

df = sns.load_dataset("mpg")

horsepower = np.array(df["horsepower"])
weight = np.array(df["weight"])
mpg = np.array(df["mpg"])


sns.scatterplot(
    x=horsepower, 
    y=mpg, 
    size=weight, 
    hue=mpg, 
    sizes=(20, 200),
    palette='rocket',
    legend=None,
)
plt.title('Relación entre Horsepower, MPG y Peso de Automóviles', fontsize=16)
plt.xlabel('Horsepower', fontsize=12)
plt.ylabel('MPG', fontsize=12)
plt.show()