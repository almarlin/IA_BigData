import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.discriminant_analysis import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.datasets import make_regression

# Creamos un dataset de regresión de 10 mil muestras
# Para simplificar la gráfica vamos a tener 1 sola caracteristica en X
# Metemos ruido en los datos
data = make_regression(n_samples=10000, n_features=1, n_informative=1, noise=30)

X = data[0]
y = data[1]

# Seleccion 80-20
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)

# Se escalan los datos
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Creamos modelo, entrenamos y predecimos
model = LinearRegression()

model.fit(X_train, y_train)

print(f'Intercepto (β0): {model.intercept_:.2f}')
print(f'Pendiente (β1): {model.coef_[0]:.2f}')

y_pred = model.predict(X_test)

resultados = pd.DataFrame({'Real': y_test, 'Predicción': y_pred})
print(resultados.head())

# Mostramos los resultados
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f'Error cuadrático medio (MSE): {mse:.2f}')
print(f'Raíz del error cuadrático medio (RMSE): {rmse:.2f}')
print(f'Coeficiente de determinación (R^2): {r2:.2f}')

# Graficamos
plt.scatter(X_test[:,0], y_test, color='blue', label='Datos reales')
plt.plot(X_test[:,0], y_pred, color='red', linewidth=2, label='Predicción (línea de regresión)')
plt.xlabel('Variable Independiente (X)')
plt.ylabel('Variable Dependiente (y)')
plt.title('Regresión Lineal: Datos reales vs Predicción')
plt.legend()
plt.show()

# RESULTADOS
# Para mejorar el desempeño del modelo habría que ajustar los hiperparámetros del mismo. 