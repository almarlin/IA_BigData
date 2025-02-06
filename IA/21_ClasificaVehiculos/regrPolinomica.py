import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
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
X_poly_train = poly.fit_transform(X_train)
X_poly_test = poly.transform(X_test)

# Ajustar el modelo de regresión polinómica
poly_model = LinearRegression()
poly_model.fit(X_poly_train, y_train)

# Hacer predicciones
y_pred_poly = poly_model.predict(X_poly_test)

# Evaluación de la regresión polinómica
print("\nEvaluación de la Regresión Polinómica (grado 2):")
print(f"MSE: {mean_squared_error(y_test, y_pred_poly):.2f}")
print(f"R^2: {r2_score(y_test, y_pred_poly):.2f}")
print(f"MAE: {mean_absolute_error(y_test, y_pred_poly):.2f}")

# Visualización de la regresión polinómica
plt.scatter(X_test["Horsepower"], y_test, color='blue', label='Datos reales')  # Usamos el conjunto de prueba para la visualización
plt.plot(X_test["Horsepower"], y_pred_poly, color='green', label='Regresión Polinómica (grado 2)')
plt.xlabel('Horsepower')
plt.ylabel('Price')
plt.title('Regresión Polinómica vs. Datos Reales')
plt.legend()
plt.savefig("regPolinomica.png")
plt.show()
