from sklearn.linear_model import LinearRegression, Ridge,Lasso
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report,mean_squared_error,r2_score
from sklearn.datasets import fetch_openml

# Cargamos los datos en un objeto bunch
data = fetch_openml(name="boston", version=1,as_frame=True)

df = data.frame
print(f"Primeras líneas del dataset:\n{df.head()}")

# Elegimos las variables de entrada y la salida
# x = df[["RM","LSTAT","AGE","TAX"]]
xs = []
xs.append(df[["RM","LSTAT"]])
xs.append(df[["RM","LSTAT","AGE","TAX"]])
y = df["MEDV"]

# Comprobamos con varias variables de entrada
for x in xs:
    print(f"Variables de entrada: {x} ------------------------------------------------------")
    # Dividimos en entrenamiento y prueba
    x_train, x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

    print("Regresión Lineal ---------------------------------------------------")
    # Creamos el modelo, entrenamos y predecimos
    modelLR = LinearRegression()
    modelLR.fit(x_train,y_train)
    y_pred = modelLR.predict(x_test)

    # Calculamos el MSE y R^2
    mse = mean_squared_error(y_true=y_test,y_pred=y_pred)   
    r2 = r2_score(y_true=y_test,y_pred=y_pred)
    print(f"Regresión Lineal | Error cuadrático medio (MSE): {mse}")
    print(f"Regresión Lineal | R^2: {r2}\n")

    # Graficamos el resultado de la predicción y la línea de perfeccion
    plt.scatter(y_test,y_pred)
    plt.plot([y_test.min(),y_test.max()],[y_test.min(),y_test.max()], color="red")
    plt.xlabel("Valores reales")
    plt.ylabel("Valores predichos")
    plt.title("Regresión lineal.")
    plt.grid(True)
    plt.show()

    print("Regresión Lasso -------------------------------------------------")
    modelLasso = Lasso()
    modelLasso.fit(x_train,y_train)
    y_pred = modelLasso.predict(x_test)

    # Calculamos el MSE y R^2
    mse = mean_squared_error(y_true=y_test,y_pred=y_pred)   
    r2 = r2_score(y_true=y_test,y_pred=y_pred)
    print(f"Regresión Lasso | Error cuadrático medio (MSE): {mse}")
    print(f"Regresión Lasso | R^2: {r2}\n")

    # Graficamos el resultado de la predicción y la línea de perfeccion
    plt.scatter(y_test,y_pred)
    plt.plot([y_test.min(),y_test.max()],[y_test.min(),y_test.max()], color="red")
    plt.xlabel("Valores reales")
    plt.ylabel("Valores predichos")
    plt.title("Regresión Lasso.")
    plt.grid(True)
    plt.show()

    print("Regresión Ridge -------------------------------------------------")
    modelRidge = Ridge()
    modelRidge.fit(x_train,y_train)
    y_pred = modelRidge.predict(x_test)

    # Calculamos el MSE y R^2
    mse = mean_squared_error(y_true=y_test,y_pred=y_pred)   
    r2 = r2_score(y_true=y_test,y_pred=y_pred)
    print(f"Regresión Ridge | Error cuadrático medio (MSE): {mse}")
    print(f"Regresión Ridge | R^2: {r2}\n")

    # Graficamos el resultado de la predicción y la línea de perfeccion
    plt.scatter(y_test,y_pred)
    plt.plot([y_test.min(),y_test.max()],[y_test.min(),y_test.max()], color="red")
    plt.xlabel("Valores reales")
    plt.ylabel("Valores predichos")
    plt.title("Regresión Ridge.")
    plt.grid(True)
    plt.show()

# Tras ejecutar por consola podemos observar como todos los modelos tienen un desempeño similar.
# Además, el aumento de variables de entrada no altera demasiado el resultado.