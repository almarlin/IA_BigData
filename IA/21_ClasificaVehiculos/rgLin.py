from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score


df = pd.read_csv("Dataset_vehiculos.csv")

# Variable independiente (X) y dependiente (y)
X = df.drop("Price",axis=1)
y = df["Price"]
# Primero, separa tus características
caracteristicas_numericas = ['Year', 'Mileage', 'EngineSize', 'Horsepower']
caracteristicas_categoricas = ['FuelType', 'Transmission']

# Prepara el preprocesamiento para características numéricas

escalador = StandardScaler()

# Prepara el preprocesamiento para características categóricas

codificador = OneHotEncoder(sparse_output=False)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Aplica el preprocesamiento
X_num_esc = escalador.fit_transform(X_train[caracteristicas_numericas])
X_cat_cod = codificador.fit_transform(X_train[caracteristicas_categoricas])

# Combina las características procesadas
X_train_procesado = np.concatenate((X_num_esc, X_cat_cod), axis=1)

# Ahora sí, crea y entrena el modelo de regresión lineal
modelo = LinearRegression()
modelo.fit(X_train_procesado, y_train)

# Para predecir, aplica el mismo preprocesamiento a los datos de prueba
X_test_num_esc = escalador.transform(X_test[caracteristicas_numericas])
X_test_cat_cod = codificador.transform(X_test[caracteristicas_categoricas])
X_test_procesado = np.concatenate((X_test_num_esc, X_test_cat_cod), axis=1)

predicciones = modelo.predict(X_test_procesado)

# Imprime el coeficiente R²
print(f'R² del modelo: {modelo.score(X_test_procesado, y_test)}')

# Calcula el MSE
mse = mean_squared_error(y_test, predicciones)
rmse = np.sqrt(mse)
print(f'MSE: {mse:.2f}')
print(f'RMSE: {rmse:.2f}')

# Muestra algunas predicciones vs valores reales
print("\nPredicciones vs Valores Reales:")
resultado = pd.DataFrame({
    'Valor Real': y_test[:5],
    'Predicción': predicciones[:5]
})
print(resultado)