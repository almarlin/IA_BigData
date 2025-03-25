import pandas as pd
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.metrics import adjusted_rand_score
from sklearn.metrics import silhouette_score


iris = load_iris()

X = iris.data
y = iris.target

df = pd.DataFrame(X, columns=iris.feature_names)
df['species'] = iris.target


kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)

# Obtener las etiquetas predichas de los clusters
labels = kmeans.labels_
df['cluster'] = labels


score = adjusted_rand_score(y, labels)
print(f'Índice de Rand ajustado: {score}')
silhouette_avg = silhouette_score(X, labels)
print(f"Silhouette Score: {silhouette_avg}")

# Graficar los clusters
plt.figure(figsize=(8, 6))
plt.scatter(df.iloc[:, 0], df.iloc[:, 1], c=df['cluster'], cmap='viridis', s=50)
plt.title('Clusters de KMeans')
plt.xlabel('Longitud del sépalo')
plt.ylabel('Ancho del sépalo')
plt.colorbar()
plt.show()

# ------------------------------------------------
# ¿Cómo se distribuyen los grupos en la gráfica?

# Los grupos en la gráfica se distribuyen en funcion del parecido de las características determinadas en X. En este caso se grafican los grupos por la longitud y el ancho del sépalo.
