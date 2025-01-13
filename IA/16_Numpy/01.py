# Alvaro Martinez Lineros CEGS IA y Big Data
# Ejercicios Numpy


import numpy as np

# Crear un vector con valores dentro del rango 10-49
print("\n--------Ejercicio 01--------")
array = np.arange(10,49,4)
print(f"Vector con valores en el rango 10-49\n{array}\n")

# Invertir vector
print("--------Ejercicio 02--------")
print(f"Array invertido\n{array[::-1]}\n")

# Crear un array de 10 ceros.
print("--------Ejercicio 03--------")
zeros = np.zeros(10)
print(f"Array con 10 ceros\n{zeros}\n")

# Crear un array de 10 unos.
print("--------Ejercicio 04--------")
unos = np.full((1,10),1)
print(f"Array con 10 unos\n{unos}\n")

# Crear matriz 3x3 con valores del 0 a 8.
print("--------Ejercicio 05--------")
tresxtres = np.arange(9).reshape(3,3)
print(f"Matriz 3x3\n{tresxtres}\n")

# Crear un array de 10 cincos.
print("--------Ejercicio 06--------")
cincos = np.full((1,10),5)
print(f"Array con 10 cincos\n{cincos}\n")

# Transformar el array anterior a dimensión [2,5] y [5,2]
print("--------Ejercicio 07--------")
a = cincos.reshape(2,5)
b = cincos.reshape(5,2)
print(f"Matrices con 10 cincos\n2x5:\n{a}\n5x2:\n{b}\n")

# Encontrar los índices (no el valor) que no son cero dentro del siguiente array: [1,2,4,2,4,0,1,0,0,0,12,4,5,6,7,0]
print("--------Ejercicio 08--------")
array = np.array([1,2,4,2,4,0,1,0,0,0,12,4,5,6,7,0])
indices = np.nonzero(array)[0]
print(f"Indices de no ceros\n{indices}\n")

# Crear una matriz identidad 6x6
print("--------Ejercicio 09--------")
identidad = np.identity(6)
print(f"Matriz identidad 6x6\n{identidad}\n")

# Crear vector con 100 valores aleatorios de formato entero.
print("--------Ejercicio 10--------")
vector = np.random.randint(1,1000,100)
print(f"Vector random de 100 valores enteros\n{vector}\n")

# Crear un array con valores al azar de forma 3x3x3 (3 dimensiones)
print("--------Ejercicio 11--------")
vector = np.random.randint(1,1000,(3,3,3))
print(f"Array random 3x3x3\n{vector}\n")

# Encontrar los valores mínimos y máximos del anterior array
print("--------Ejercicio 12--------")
max = vector.max()
min = vector.min()
print(f"Máximo del anterior array:\n{max}\nMinimo del anterior array:\n{min}\n")

# Indicar los índices (posición) de los valores mínimos y máximos del array
print("--------Ejercicio 13--------")
idxmax = np.argmax(vector)
idxmin = np.argmin(vector)
print(f"Indice del máximo del anterior array:\n{idxmax}\nIndice del minimo del anterior array:\n{idxmin}\n")

# Generar una matriz de tamaño 10x10 en la que los bordes sean 1 y el interior ceros (0). (Utilizar rangos de índices)
print("--------Ejercicio 14--------")
matriz = np.zeros((10, 10))
matriz[0,:] = 1
matriz[-1, :] = 1
matriz[:, 0] = 1
matriz[:, -1] = 1
print(f"Matriz 10x10:\n{matriz}\n")

# Crear array de tamaño 5x5 con los siguientes valores; [0,1,2,3,4]
print("--------Ejercicio 15--------")
vector = np.random.randint(0,5,(5,5))
print(f"Array 5x5:\n{vector}\n")

# Crear dos arrays aleatorios del mismo tamaño (3x3 o 5x5) y verificar si son iguales. Comprobar si algún elemento coincide, generando matriz booleana.
print("--------Ejercicio 16--------")
matriz1 = np.random.randint(0,5,(5,5))
matriz2 = np.random.randint(0,5,(5,5))
iguales = np.array_equal(matriz1,matriz2)
print(f"Matriz1:\n{matriz1}\nMatriz2:\n{matriz2}\n")
booleana = matriz1 == matriz2
print(f"Las matrices son iguales:\n{iguales}\nMatriz booleana:\n{booleana}\n")

# Generar array de dimensión 5x5 en el que los elementos sean de tipo numérico entero aleatorio comprendido entre el 1 y 100.
print("--------Ejercicio 17--------")
matriz = np.random.randint(1,100,(5,5))
print(f"Matriz 5x5 de 1 a 100\n{matriz}\n")

# Dado el array anterior, obtener la suma total de la matriz 5x5.
print("--------Ejercicio 18--------")
suma = matriz.sum()
print(f"Suma total de la matriz\n{suma}\n")
# Dado el array anterior, obtener un nuevo array que contenga la suma de cada una de las columnas.
print("--------Ejercicio 19--------")
suma = matriz.sum(axis=0)
print(f"Suma total de las columnas de la matriz\n{suma}\n")

# Dado el array anterior, extraer fila inicial, fila intermedia (fila 3) y la última fila.
print("--------Ejercicio 20--------")
fila1 = matriz[0]
idxmedio = matriz.shape[0]
idxmedio = int(idxmedio/2)
fila2 = matriz[idxmedio]
fila3 = matriz[-1]
print(f"Filas de la matriz\n{fila1}\n{fila2}\n{fila3}\n")
