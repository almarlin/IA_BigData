import pandas as pd

rondas = [
    "Ronda 1",
    "Ronda 2",
    "Ronda 3",
    "Ronda 4",
    "Ronda 5",
    "Ronda 6",
    "Ronda 7",
    "Ronda 8",
]
puntuaciones = []

print("Introduce las puntuaciones del jugador en 8 rondas del juego:")

for ronda in rondas:

    puntuacion = int(input(f"Puntuación en {ronda}: "))
    puntuaciones.append(puntuacion)


puntuaciones_serie = pd.Series(puntuaciones, index=rondas)

puntuacion_maxima = puntuaciones_serie.max()
puntuacion_minima = puntuaciones_serie.min()
diferencia = puntuacion_maxima - puntuacion_minima

print(f"\nPuntuación máxima: {puntuacion_maxima}")
print(f"Puntuación mínima: {puntuacion_minima}")
print(f"Diferencia entre la puntuación máxima y mínima: {diferencia}")

rondas_mayores_80 = puntuaciones_serie[puntuaciones_serie > 80]
print(f"\nRondas con puntuación superior a 80:\n{rondas_mayores_80}")

ranking = puntuaciones_serie.sort_values()
print("\nRanking de las puntuaciones de menor a mayor:")
print(ranking)
