import pandas as pd

semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
ventas = []
print("\nIntroduce las ventas de la semana:\n")

for dia in semana:
    ventas.append(float(input(f"Ventas del {dia}:\n")))


ventasSerie = pd.Series(ventas,semana)
print(f"Total de ventas: {ventasSerie.sum()}")
print(f"Promedio de ventas: {ventasSerie.mean()}")
print(f"Dia con las mayores ventas: {ventasSerie.idxmax()} | {ventasSerie.max()}")