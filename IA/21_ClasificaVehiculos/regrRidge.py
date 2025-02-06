import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

df = pd.read_csv("Dataset_vehiculos.csv")

# Variable independiente (X) y dependiente (y)
X = df[["Horsepower", "Mileage", "Year"]]
y = df["Price"]

# Dividir en conjunto de entrenamiento (80%) y prueba (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Transformar las características a un polinomio de grado 2
poly = PolynomialFeatures(degree=2)
X_poly_train = poly.fit_transform(X_train)  # Aplicamos la transformación en el conjunto de entrenamiento
X_poly_test = poly.transform(X_test)        # Aplicamos la transformación en el conjunto de prueba

# Ajustar el modelo de regresión Ridge con un parámetro de regularización (alpha)
ridge_model = Ridge(alpha=1.0)  # El parámetro alpha controla la cantidad de regularización
ridge_model.fit(X_poly_train, y_train)  # Entrenamos el modelo con los datos transformados

# Hacer predicciones
y_pred_ridge = ridge_model.predict(X_poly_test)  # Realizamos las predicciones sobre el conjunto de prueba

# Evaluación de la regresión Ridge
print("\nEvaluación de la Regresión Ridge (con regularización):")
print(f"MSE: {mean_squared_error(y_test, y_pred_ridge):.2f}")
print(f"R^2: {r2_score(y_test, y_pred_ridge):.2f}")
print(f"MAE: {mean_absolute_error(y_test, y_pred_ridge):.2f}")

# Visualización de la regresión Ridge
plt.scatter(X_test["Mileage"], y_test, color='blue', label='Datos reales')  # Usamos el conjunto de prueba para la visualización
plt.plot(X_test["Mileage"], y_pred_ridge, color='red', label='Regresión Ridge')
plt.xlabel('Mileage')
plt.ylabel('Price')
plt.title('Regresión Ridge vs. Datos Reales')
plt.legend()
plt.savefig("regrRidge.png")
plt.show()
