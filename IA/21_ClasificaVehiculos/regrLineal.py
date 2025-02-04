#PASO 01. IMPORTAR LIBRERIAS NECESARIAS
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler,OneHotEncoder


df = pd.read_csv("Dataset_vehiculos.csv")

# Variable independiente (X) y dependiente (y)
X = df.drop("Price",axis=1)
y = df["Price"]

plt.figure(figsize=(10, 6))
sns.histplot(df['Price'], kde=True)
plt.title('Distribución del precio')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.show()

print(f'Valores nulos:\n{df.isnull().sum()}')

#PASO 03. DIVIDIR LOS DATOS EN ENTRENAMIENTO Y PRUEBA
# Dividir en conjunto de entrenamiento (80%) y prueba (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
x_train = scaler.fit_transform(X_train)
x_test = scaler.transform(X_test)

print(f'Tamaño del conjunto de entrenamiento: {x_train.shape[0]} muestras')
print(f'Tamaño del conjunto de prueba: {x_test.shape[0]} muestras')


#PASO 04. CREAR Y ENTRENAR EL MODELO DE REGRESIÓN LINEAL
# Crear el modelo de regresión lineal
model = LinearRegression()

# Entrenar el modelo con los datos de entrenamiento
model.fit(x_train, y_train)

# Obtener los coeficientes aprendidos
print(f'Intercepto (β0): {model.intercept_:.2f}')
print(f'Pendiente (β1): {model.coef_[0]:.2f}')


#PASO 05. REALIZAR PREDICCIONES
# Realizar predicciones sobre el conjunto de prueba
y_pred = model.predict(x_test)

# Comparar predicciones con valores reales
resultados = pd.DataFrame({'Real': y_test, 'Predicción': y_pred})
print(resultados.head())


#PASO 06. EVALUAR EL MODELO
# Calcular métricas de rendimiento
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f'Error cuadrático medio (MSE): {mse:.2f}')
print(f'Raíz del error cuadrático medio (RMSE): {rmse:.2f}')
print(f'Coeficiente de determinación (R^2): {r2:.2f}')


#PASO 07. VISUALIZACIÓN DE RESULTADOS
# Graficar datos reales vs predicciones
plt.scatter(x_test, y_pred, color='blue', label='Datos reales vs predicción')
# Línea de perfección (donde la predicción sería igual al valor real)
plt.plot([x_test.min(), x_test.max()], [y_test.min(), y_test.max()], color='red', linewidth=2, label='Línea de perfección')
plt.xlabel('Precio real')
plt.ylabel('Precio predicho')
plt.title('Regresión Lineal: Datos reales vs Predicción')
plt.legend()
plt.show()

