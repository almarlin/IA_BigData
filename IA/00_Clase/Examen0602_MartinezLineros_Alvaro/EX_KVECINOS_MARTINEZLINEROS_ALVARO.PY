import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Cargamos los datos
iris = load_iris()
X = iris.data
y = iris.target


# Dividimos 80%-20%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Se escalan los datos
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Creamos el modelo, entrenamos y predecimos
knn = KNeighborsClassifier(n_neighbors=3, metric='euclidean')
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)

# Se muestran las métricas
accuracy = accuracy_score(y_test, y_pred)
print(f'Precisión del modelo: {accuracy:.2f}')

print("Matriz de confusión:")
print(confusion_matrix(y_test, y_pred))
print("Reporte de clasificación:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

#  RESULTADOS
# El valor de K varía los resultados en tanto que un menor número de vecinos puede causar
# overfitting, sin embargo, viendo que el tamaño de la muestra test son 30, un valor de 3
# sigue dando una precisión perfecta. Esto puede estar causado porque el modelo se haya adaptado
# demasiado bien a los datos de entrenamiento