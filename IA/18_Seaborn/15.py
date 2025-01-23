import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix

# Mapa de calor de confusión para clasificación

n_samples = 100

real = np.random.choice([0, 1], size=n_samples)

predicha = np.random.choice([0, 1], size=n_samples)

df = pd.DataFrame({
    'real': real,
    'predicha': predicha
})

cm = confusion_matrix(real,predicha)

sns.heatmap(data=cm,annot=True,fmt='g')
plt.title("Mapa de calor de confusión para clasificación")
plt.xlabel('Predicción')
plt.ylabel('Real')
plt.show()

