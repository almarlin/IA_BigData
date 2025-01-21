import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Distribución de datos con KDE Plot y rug plot

df = sns.load_dataset("tips")

total_bill = df["total_bill"].dropna()
tip = df["tip"].dropna()

sns.kdeplot(total_bill,label="Total bill KDE",fill=True)
sns.kdeplot(tip,label="Tip KDE",fill=True)
sns.rugplot(total_bill,label="Total bill rug")
sns.rugplot(tip,label="Tip rug")
plt.title("Distribucion de datos con KDE y rug plot")
plt.legend()
plt.show()
