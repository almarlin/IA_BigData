import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score

import pandas as pd
import numpy as np

# Fijar la semilla para reproducibilidad
np.random.seed(42)

# Generar datos
n_samples = 1000

# Años entre 2000 y 2022
years = np.random.randint(2000, 2023, size=n_samples)

# Kilometraje entre 10000 y 300000
mileage = np.random.randint(10000, 300001, size=n_samples)

# Tamaño del motor entre 1.0 y 6.0
engine_size = np.round(np.random.uniform(1.0, 6.0, size=n_samples), 1)

# Potencia entre 50 y 500
horsepower = np.random.randint(50, 501, size=n_samples)

# Generar precios con una relación lineal más algo de ruido
price = (2000 * (2022 - years) + 
         (-0.05 * mileage) + 
         (10000 * engine_size) + 
         (100 * horsepower) + 
         np.random.normal(0, 10000, size=n_samples))

# Crear el DataFrame
df_simulated = pd.DataFrame({
    'ID': range(1, n_samples + 1),
    'Year': years,
    'Mileage': mileage,
    'EngineSize': engine_size,
    'Horsepower': horsepower,
    'Price': price
})

df = df_simulated

# Seleccionar características y variable objetivo
X = df[['Year', 'Mileage', 'EngineSize', 'Horsepower']]
y = df['Price']

# Dividir el conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=50)

# Normalizar los datos
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Crear el modelo de Random Forest
model =  LinearRegression()


# Entrenar el modelo
model.fit(X_train_scaled, y_train)

# Hacer predicciones
y_pred = model.predict(X_test_scaled)

# Evaluar el modelo
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Squared Error: {mse}')
print(f'R^2 Score: {r2}')



plt.scatter(X_test, y_pred, color='blue', label='Predicciones')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linewidth=2, label='Línea de perfección')
plt.show()