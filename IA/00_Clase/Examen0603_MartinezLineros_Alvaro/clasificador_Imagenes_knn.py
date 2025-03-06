from sklearn.datasets import fetch_openml
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


# Cargar el conjunto de datos MNIST
mnist = fetch_openml('mnist_784')

x = np.array(mnist.data)
y = np.array(mnist.target)

# Definimos conjunto de entrenamiento y prueba
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

# Comprobamos las precisiones para el distinto numero de vecinos
neighbors = [1,3,5,7,9]
precisiones = []
for n in neighbors:
    # Creamos el modelo y lo entrenamos con los datos de prueba
    model = KNeighborsClassifier(n_neighbors=n,metric='euclidean',weights='distance')
    model.fit(x_train,y_train)

    # Hacemos la predicción
    y_pred = model.predict(x_test)
    prec = accuracy_score(y_pred,y_test)
    # Añadimos la precisión obtenida a la lista y la mostramos por consola
    precisiones.append(prec)
    print(f"Precisión con {n} vecinos: {prec}")

# Creamos el modelo con k=3 para hacer el reporte y la matriz
model = KNeighborsClassifier(n_neighbors=3,metric='euclidean',weights='distance')
model.fit(x_train,y_train)

y_pred = model.predict(x_test)

# Creamos el reporte y la matriz
matriz = confusion_matrix(y_pred=y_pred,y_true=y_test)
report = classification_report(y_pred=y_pred,y_true=y_test)
print(f"Matriz de confusion (k=3):\n{matriz}")
print(f"Reporte de clasificación (k=3):\n{report}")

# Visualizamos la relación entre número de vecinos y precisión del modelo
plt.bar(neighbors,precisiones)
plt.xlabel("Número de vecinos")
plt.ylabel("Precisión alcanzada")
plt.title("Precisión del modelo por número de vecinos.")
plt.grid(True)
plt.show()




