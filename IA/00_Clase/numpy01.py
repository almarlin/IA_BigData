import numpy as np  # type: ignore

a3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a3)

a1 = np.zeros([3, 3, 3])
print(a1)

a9 = np.full([2, 3], 5)
print(a9)

# inicio, fin, salto
a2 = np.arange(1, 20, 2)
print(a2)

a4 = np.random.random([5, 4])
# Numero de dimensiones
print(a4.ndim)
# Elementos
print(a4.shape)

# TODOS LOS ELEMENTOS DEBEN TENER EL MISMO TIPO

# OPERACIONES MATEMATICAS CON ARRAYS
# SUMA
array1 = np.array([2, 3, 4])
array2 = np.array([6, 7, 8])
print(array1 + array2)

# RESTA
array1 = np.array([2, 3, 4])
array2 = np.array([6, 7, 8])
print(array1 - array2)

# PRODUCTO
array1 = np.array([[2, 3, 4], [2, 5, 8], [2, 5, 8]])
array2 = np.array([[6, 7, 8], [2, 5, 9], [2, 5, 9]])
print(array1 * array2)

# Traspuesta
array3 = np.array([[2, 3, 4], [2, 5, 8]])
print(array3, "\n", array3.T)

# Determinante
print(np.linalg.det(array1))
array4 = np.array([[1, 2], [3, 4]])
print(np.linalg.det(array4))

# Diagonal principal
print(array1.trace())
# Inversa
print(np.linalg.inv(array4))

# SISTEMAS DE ECUACIONES
# x + 2y = 1
# 3x + 5y = 2
# Se generan 2 listas con las incognitas y las soluciones
a = np.array([[1,2],[3,5]])
b = np.array([1,2])

print(np.linalg.solve(a,b))

