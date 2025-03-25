import numpy as np
import random

# Definir las longitudes de los segmentos del brazo robótico
L1 = 5  # Longitud del primer segmento
L2 = 3  # Longitud del segundo segmento

# Función para calcular los ángulos de las articulaciones (cinemática inversa)
def calcular_angulos(x, y):
    # Calcular el ángulo de la segunda articulación (theta2)
    cos_theta2 = (x**2 + y**2 - L1**2 - L2**2) / (2 * L1 * L2)
    
    # Validar que la posición es alcanzable, si no lo es, retornamos None
    if abs(cos_theta2) > 1:
        return None
    
    # Calcular theta2 usando la función arcocoseno
    theta2 = np.arccos(cos_theta2)

    # Calcular theta1 usando la ecuación de la cinemática inversa
    theta1 = np.arctan2(y, x) - np.arctan2(L2 * np.sin(theta2), L1 + L2 * np.cos(theta2))

    return np.degrees(theta1), np.degrees(theta2)

# Generar 10 posiciones aleatorias y calcular los ángulos para cada una
resultados = []
for _ in range(10):
    # Generar posiciones aleatorias dentro de un rango
    x = random.uniform(-L1-L2, L1+L2)
    y = random.uniform(-L1-L2, L1+L2)
    
    # Calcular los ángulos correspondientes a la posición generada
    angulos = calcular_angulos(x, y)
    
    # Verificar si la posición es alcanzable
    if angulos is not None:
        resultados.append((x, y, angulos[0], angulos[1]))
    else:
        resultados.append((x, y, "No alcanzable", "No alcanzable"))

# Imprimir los resultados en formato tabla
print("\nPosición Final (x, y)    | Ángulo 1 (θ1) | Ángulo 2 (θ2)")
print("---------------------------------------------------------")
for resultado in resultados:
    # Verificar si los resultados son alcanzables
    if isinstance(resultado[2], str):
        print(f"({resultado[0]:.2f}, {resultado[1]:.2f})    | {resultado[2]}    | {resultado[3]}")

    else:
        print(f"({resultado[0]:.2f}, {resultado[1]:.2f})    | {resultado[2]:.2f}°       | {resultado[3]:.2f}°")

