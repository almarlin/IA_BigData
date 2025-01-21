import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

ventas_mes = pd.read_csv("09.csv")

df = pd.DataFrame(ventas_mes)

meses = df['Mes']
dias = df['Día']
ventas = df['Ventas']

plt.figure(figsize=(14, 7))

sns.lineplot(data=df, x='Día', y='Ventas', hue='Mes', palette='tab20', marker='o', 
             linestyle='-', linewidth=2, ci=95)

plt.title('Ventas Diarias por Mes con Tendencias Estacionales', fontsize=16)
plt.xlabel('Día del Mes', fontsize=12)
plt.ylabel('Ventas', fontsize=12)
plt.xticks(range(1, 32), rotation=45)
plt.legend(title='Meses', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()
