import numpy as np
import matplotlib.pyplot as plt


def matriz_transformacion(theta, d):
    return np.array([
        [np.cos(theta), -np.sin(theta), d * np.cos(theta)],
        [np.sin(theta), np.cos(theta), d * np.sin(theta)],
        [0, 0, 1]
    ])


# Longitudes de los segmentos del brazo
L1 = 5  # Primer segmento
L2 = 3  # Segundo segmento

# Ángulos de las articulaciones (en radianes)
theta1 = np.radians(30)  # Primera articulación
theta2 = np.radians(45)  # Segunda articulación


# Matrices de transformación
T1 = matriz_transformacion(theta1, L1)
T2 = matriz_transformacion(theta2, L2)

# Producto de las matrices para obtener la posición final
T_total = np.dot(T1, T2)

# Posición final del efector
pos_final = T_total[:2, 2]
print(f"1 Posición final del efector: {pos_final}")


# Coordenadas de los puntos
x0, y0 = 0, 0  # Origen
x1, y1 = L1 * np.cos(theta1), L1 * np.sin(theta1)  # Primer segmento
x2, y2 = x1 + L2 * np.cos(theta1 + theta2), y1 + L2 * np.sin(theta1 + theta2)  # Segundo segmento

# Graficar el brazo robótico
plt.plot([x0, x1], [y0, y1], label="Segmento 1")
plt.plot([x1, x2], [y1, y2], label="Segmento 2")
plt.scatter([x0, x1, x2], [y0, y1, y2], color='red')
plt.xlim(-L1-L2-1, L1+L2+1)
plt.ylim(-L1-L2-1, L1+L2+1)
plt.gca().set_aspect('equal', adjustable='box')
plt.title('Brazo Robótico 2 DOF')
plt.legend()
plt.grid(True)
plt.show()


theta1 = np.radians(15)
theta2 = np.radians(120)

# Matrices de transformación
T1 = matriz_transformacion(theta1, L1)
T2 = matriz_transformacion(theta2, L2)

# Producto de las matrices para obtener la posición final
T_total = np.dot(T1, T2)

# Posición final del efector
pos_final = T_total[:2, 2]
print(f"2 Posición final del efector: {pos_final}")


# Coordenadas de los puntos
x0, y0 = 0, 0  # Origen
x1, y1 = L1 * np.cos(theta1), L1 * np.sin(theta1)  # Primer segmento
x2, y2 = x1 + L2 * np.cos(theta1 + theta2), y1 + L2 * np.sin(theta1 + theta2)  # Segundo segmento

# Graficar el brazo robótico
plt.plot([x0, x1], [y0, y1], label="Segmento 1")
plt.plot([x1, x2], [y1, y2], label="Segmento 2")
plt.scatter([x0, x1, x2], [y0, y1, y2], color='red')
plt.xlim(-L1-L2-1, L1+L2+1)
plt.ylim(-L1-L2-1, L1+L2+1)
plt.gca().set_aspect('equal', adjustable='box')
plt.title('Brazo Robótico 2 DOF')
plt.legend()
plt.grid(True)
plt.show()