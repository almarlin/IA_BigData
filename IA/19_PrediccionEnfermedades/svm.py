import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.inspection import permutation_importance

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
model = SVC(kernel='rbf', C=1.0, gamma='scale')
model.fit(x_train, y_train)


y_pred = model.predict(x_test)

y_pred = model.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Precisión del modelo: {accuracy:.2f}')

conf_matrix = confusion_matrix(y_test, y_pred)
print("Matriz de confusión:")
print(conf_matrix)

print("Reporte de clasificación:")
print(classification_report(y_test, y_pred, target_names=['No enfermo', 'Enfermo']))

# Realizar la importancia por permutación
result = permutation_importance(model, x_test, y_test, n_repeats=10, random_state=42, n_jobs=-1)

# Obtener la importancia promedio de cada característica
coef_df = pd.DataFrame(result.importances_mean, columns=['Importancia'], index=x.columns)

# Mostrar la importancia de las características
print(f"Importancia de las características:\n{coef_df}")

fig, diagrama = plt.subplots(2, 1, figsize=(15,15))
diagrama[0].bar(['No enfermo', 'Enfermo'], np.bincount(y_pred))
diagrama[0].set_xlabel('Clase Predicha')
diagrama[0].set_ylabel('Frecuencia')
diagrama[0].set_title('Distribución de Predicciones')

coef_df['Importancia'].plot(kind='barh', ax=diagrama[1], figsize=(8, 6), color='skyblue')
diagrama[1].set_title("Importancias de SVM")
diagrama[1].set_xlabel("Importancias")
diagrama[1].set_ylabel("Características")
diagrama[1].set_yticks(range(len(coef_df)))
diagrama[1].set_yticklabels(coef_df.index, rotation=45)
plt.tight_layout()
plt.savefig('svm_resultados.png', format='png')
plt.show()