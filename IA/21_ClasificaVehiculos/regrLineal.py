import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score,mean_absolute_error
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from scipy import stats


df = pd.read_csv("Dataset_vehiculos.csv")

# Variable independiente (X) y dependiente (y)
X = df[["Horsepower","Mileage","Year"]]
y = df["Price"]


print(f'Valores nulos:\n{df.isnull().sum()}')

# Dividir en conjunto de entrenamiento (80%) y prueba (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f'Tamaño del conjunto de entrenamiento: {X_train.shape[0]} muestras')
print(f'Tamaño del conjunto de prueba: {X_test.shape[0]} muestras')

# Crear el modelo de regresión lineal
model = LinearRegression()

# Entrenar el modelo con los datos de entrenamiento
model.fit(X_train, y_train)

# Obtener los coeficientes aprendidos
print(f'Intercepto (β0): {model.intercept_:.2f}')
print(f'Pendiente (β1): {model.coef_[0]:.2f}')

# Realizar predicciones sobre el conjunto de prueba
y_pred = model.predict(X_test)

# Comparar predicciones con valores reales
resultados = pd.DataFrame({'Real': y_test, 'Predicción': y_pred})
print(resultados.head())


# Calcular métricas de rendimiento
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Error cuadrático medio (MSE): {mse:.2f}')
print(f'Error absoluto medio (MAE): {mae:.2f}')
print(f'Coeficiente de determinación (R^2): {r2:.2f}')

# Crear un gráfico de dispersión de los valores reales vs las predicciones
plt.figure(figsize=(10, 6))
plt.scatter(X_test["Horsepower"], y_test, color='blue', label='Predicciones')
plt.plot(X_test["Horsepower"],y_pred, color='red', linewidth=2, label='Línea de perfección')

plt.title('Valores Reales vs Predicciones')
plt.xlabel('Precio Real')
plt.ylabel('Precio Predicho')
plt.legend()
plt.grid(True)
plt.savefig("regLineal.png")
plt.show()


