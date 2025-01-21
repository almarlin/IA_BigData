import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# FacetGrid con múltiples gráficos de distribución

df = sns.load_dataset("fmri")

tiempo=np.array(df["timepoint"])
senyal=np.array(df["signal"])

g = sns.FacetGrid(df, col="subject", col_wrap=4, height=4)

g.map(sns.kdeplot, "signal", "timepoint")

g.set_axis_labels("Señal", "Tiempo")
g.set_titles("{col_name}")
plt.show()