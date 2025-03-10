import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker


data = pd.read_excel("Financial_Sample.xlsx")


# 1. Exploración inicial del dataset
# Pregunta: ¿Cuántas filas y columnas tiene el dataset? 700x16 ¿Qué tipo de información contiene cada columna?
# Identificar las columnas y describir brevemente qué tipo de datos contienen (por ejemplo, segmento, país, producto, etc.).

print(
    f"Descripción básica del dataset:\n{data.describe()}\n\nInformación del dataset:\n"
)
print(f"\n{data.info()}")

# 3. Segmentación por categorías
# Pregunta: ¿Cómo se distribuyen las ventas por segmento (Government, Midmarket, Channel Partners, etc.)? ¿Qué segmento tiene el mayor volumen de ventas?
# Agrupar los datos por segmento y que calcular el total de ventas para cada uno. Luego, visualizar estos datos en un gráfico.

distribucion = pd.DataFrame()

distribucion["Segment"] = data["Segment"].unique()

for segmento in distribucion["Segment"]:
    distribucion.loc[distribucion["Segment"]==segmento, "Profit"] = data[data["Segment"]==segmento]["Profit"].sum()

print(distribucion)

plt.bar(distribucion["Segment"], distribucion["Profit"])
ax = plt.gca()
formatter = mticker.FuncFormatter(lambda x, _: f"{x:,.0f}")
ax.yaxis.set_major_formatter(formatter)

plt.axhline(0, color='red', linewidth=1)
plt.ylabel("Beneficios")
plt.xlabel("Segmento")
plt.title("Beneficios por segmento")
plt.show()

# 4. Análisis por país
# Pregunta: ¿Qué país tiene el mayor volumen de ventas? ¿Y el menor?
# Agrupar los datos por país y que calcular el total de ventas para cada uno. Luego, identificar el país con mayores y menores ventas.

distribucion = pd.DataFrame()

distribucion["Country"] = data["Country"].unique()

for country in distribucion["Country"]:
    distribucion.loc[distribucion["Country"]==country, "Units Sold"] = data[data["Country"]==country]["Units Sold"].sum()

print(distribucion)
fig, ax = plt.subplots()

# Gráfico de pastel con etiquetas de países y porcentajes
wedges, texts, autotexts = ax.pie(
    distribucion["Units Sold"],
    labels=distribucion["Country"],
    autopct="%1.1f%%",
    startangle=140,
    wedgeprops={'edgecolor': 'black'}
)

for text in texts:
    text.set_fontsize(10)
for autotext in autotexts:
    autotext.set_fontsize(10)
    autotext.set_color("white")

ax.legend(wedges, distribucion["Country"], title="Países", loc="center left", bbox_to_anchor=(1, 0.5))
plt.title("Volumen de ventas por paises")
plt.show()