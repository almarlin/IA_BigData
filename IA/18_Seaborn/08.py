import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Pairplot para el análisis multivariado

df = sns.load_dataset("iris")

sepal_length = np.array(df["sepal_length"])
sepal_width = np.array(df["sepal_width"])
petal_length = np.array(df["petal_length"])
petal_width = np.array(df["petal_width"])


pairplot = sns.pairplot(
    df, hue="species", kind="scatter", diag_kind="kde", markers=["o", "s", "D"]
)

pairplot.map_lower(
    sns.regplot, scatter_kws={"s": 50, "alpha": 0.6}, line_kws={"color": "red", "lw": 2}
)
plt.show()
