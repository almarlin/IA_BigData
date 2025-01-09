import pandas as pd
import matplotlib.pyplot as plt

calificaciones = []
print("Introduce las calificaciones de satisfacción (de 1 a 5) de 12 clientes:")

for i in range(1, 13):
    while True:
        try:
            calificacion = int(input(f"Calificación del cliente {i}: "))
            if calificacion < 1 or calificacion > 5:
                print("Por favor ingresa una calificación entre 1 y 5.")
            else:
                calificaciones.append(calificacion)
                break
        except ValueError:
            print("Por favor ingresa un valor numérico válido.")

calificaciones_serie = pd.Series(calificaciones)

frecuencia = calificaciones_serie.value_counts().sort_index()

clientes_satisfechos = (calificaciones_serie >= 4).sum()
porcentaje_satisfechos = (clientes_satisfechos / len(calificaciones_serie)) * 100
calificaciones_serie_reemplazada = calificaciones_serie.replace(1, "Insatisfecho")

print(f"\nFrecuencia de cada calificación:")
print(frecuencia)

print(f"\nPorcentaje de clientes satisfechos (calificación ≥ 4): {porcentaje_satisfechos:.2f}%")

print("\nCalificaciones con los valores reemplazados:")
print(calificaciones_serie_reemplazada)

plt.figure(figsize=(8, 6))
frecuencia.plot(kind="bar", color="skyblue")
plt.title("Frecuencia de Calificaciones de Satisfacción")
plt.xlabel("Calificación")
plt.ylabel("Número de Clientes")
plt.xticks(rotation=0)
plt.grid(axis="y")
plt.show()
