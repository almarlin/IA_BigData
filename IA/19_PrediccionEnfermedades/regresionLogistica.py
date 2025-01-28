import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report



df_cardiaca = pd.read_csv("Dataset_Enfermedades.csv")

x = df_cardiaca.drop("enfermedad_cardiaca",axis=1) # Datos utilizados para predecir
y = df_cardiaca["enfermedad_cardiaca"] # Datos a predecir


# Seleccionamos el 80% de los datos para entrenar al modelo y el 20% restante servirá para ponerlo a prueba
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Normalizamos los datos
scaler = StandardScaler()
x_train = scaler.fit_transform(X_train)
x_test = scaler.transform(X_test)

# Creamos y entrenamos el modelo
model = LogisticRegression()
model.fit(x_train, y_train)

# Pedimos al modelo que prediga sobre los datos de test
y_pred = model.predict(x_test)


# Evaluamos el modelo

# Se calcula la precision
accuracy = accuracy_score(y_test, y_pred)
print(f'Precisión del modelo: {accuracy:.2f}')
# Matriz de confusión
conf_matrix = confusion_matrix(y_test, y_pred)
print("Matriz de confusión:")
print(conf_matrix)

# Reporte de clasificación
print("Reporte de clasificación:")
print(classification_report(y_test, y_pred, target_names=['No enfermo', 'Enfermo']))

# Mostrar los coeficientes junto con los nombres de las características
coef = model.coef_
coef_df = pd.DataFrame(coef.T, columns=['Coeficiente'], index=x.columns)
print(f"Coeficientes de las características:\n{coef_df}")

# Visualización de la distribución de predicciones y resultados reales
fig, diagrama = plt.subplots(3, 1, figsize=(15,15))

# Distribución de las predicciones
diagrama[0].bar(['No enfermo', 'Enfermo'], np.bincount(y_pred))
diagrama[0].set_xlabel('Clase Predicha')
diagrama[0].set_ylabel('Frecuencia')
diagrama[0].set_title('Distribución de Predicciones')

# Distribución de las clases reales
diagrama[1].bar(['No enfermo', 'Enfermo'], np.bincount(y_test))
diagrama[1].set_xlabel('Clase Real')
diagrama[1].set_ylabel('Frecuencia')
diagrama[1].set_title('Distribución de Clases Reales')

# Coeficientes de la regresión logística
coef_df['Coeficiente'].plot(kind='bar', ax=diagrama[2], figsize=(8, 6), color='skyblue')
diagrama[2].set_title("Coeficientes de la Regresión Logística")
diagrama[2].set_ylabel("Coeficiente")
diagrama[2].set_xlabel("Características")
diagrama[2].set_xticks(range(len(coef_df)))
diagrama[2].set_xticklabels(coef_df.index, rotation=45)

# Mostrar los gráficos
plt.tight_layout()

plt.savefig('regresion_resultados.png', format='png')

plt.show()