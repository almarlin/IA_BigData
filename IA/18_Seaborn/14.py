import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Plot de violín combinado con stripplot

df = sns.load_dataset("titanic")

age = np.array(df["age"])
clase = np.array(df["class"])


sns.violinplot(x=clase,y=age,fill=False)
sns.stripplot(x=clase,y=age,jitter=True,alpha=0.5)
plt.title("Plot de violín combinado con stripplot")
plt.show()