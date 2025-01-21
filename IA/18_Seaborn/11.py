import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd


# Swarmplot con ajuste de jitter

df = sns.load_dataset("penguins")

flipper_length = np.array(df["flipper_length_mm"])
body_mass = np.array(df["body_mass_g"])

sns.swarmplot(data=df,x=flipper_length,y=body_mass,dodge=True,size=2)

plt.title("Relación entre Longitud de Aletas y Peso Corporal de los Pingüinos", fontsize=16)
plt.xlabel("Longitud de Aletas (mm)", fontsize=12)
plt.ylabel("Peso Corporal (g)", fontsize=12)
plt.tight_layout()
plt.show()
