import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pandas as pd

df_cardiaca = pd.read_csv("Dataset_Enfermedades.csv")

x = df_cardiaca.drop("enfermedad_cardiaca",axis=1) # Datos utilizados para predecir
y = df_cardiaca["enfermedad_cardiaca"] # Datos a predecir

# Seleccionamos el 80% de los datos para entrenar al modelo y el 20% restante servirá para ponerlo a prueba
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Normalizamos los datos
scaler = StandardScaler()
x_train = scaler.fit_transform(X_train)
x_test = scaler.transform(X_test)

# Creamos el modelo
tree_clf = DecisionTreeClassifier(criterion='gini', max_depth=3, random_state=42)
tree_clf.fit(x_train, y_train)

y_pred = tree_clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Precisión del modelo: {accuracy:.2f}')

conf_matrix = confusion_matrix(y_test, y_pred)
print("Matriz de confusión:")
print(conf_matrix)

print("Reporte de clasificación:")
print(classification_report(y_test, y_pred, target_names=['No enfermo', 'Enfermo']))

# Mostrar la Importancia junto con los nombres de las características
coef = tree_clf.feature_importances_
coef_df = pd.DataFrame(coef.T, columns=['Importancia'], index=x.columns)
print(f"Importancia de las características:\n{coef_df}")

plt.figure(figsize=(12, 12))
plot_tree(tree_clf, feature_names=x.columns, class_names=['No enfermo', 'Enfermo'], filled=True)
plt.title("Árbol de Decisión - Enfermedades cardíacas")
plt.savefig('arbol_resultados.png', format='png')
plt.show()