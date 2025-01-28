import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
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

# Creamos el modelo
rf_model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
rf_model.fit(x_train, y_train)

y_pred = rf_model.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Precisión del modelo: {accuracy:.2f}')

conf_matrix = confusion_matrix(y_test, y_pred)
print("Matriz de confusión:")
print(conf_matrix)

print("Reporte de clasificación:")
print(classification_report(y_test, y_pred, target_names=['No enfermo', 'Enfermo']))

# Mostrar la Importancia junto con los nombres de las características
coef = rf_model.feature_importances_
coef_df = pd.DataFrame(coef.T, columns=['Importancia'], index=x.columns)
print(f"Importancia de las características:\n{coef_df}")


fig, diagrama = plt.subplots(2, 1, figsize=(15,15))
diagrama[0].bar(['No enfermo', 'Enfermo'], np.bincount(y_pred))
diagrama[0].set_xlabel('Clase Predicha')
diagrama[0].set_ylabel('Frecuencia')
diagrama[0].set_title('Distribución de Predicciones')

coef_df['Importancia'].plot(kind='barh', ax=diagrama[1], figsize=(8, 6), color='skyblue')
diagrama[1].set_title("Importancias de random forest")
diagrama[1].set_xlabel("Importancias")
diagrama[1].set_ylabel("Características")
diagrama[1].set_yticks(range(len(coef_df)))
diagrama[1].set_yticklabels(coef_df.index, rotation=45)
plt.tight_layout()
plt.savefig('rf_resultados.png', format='png')
plt.show()