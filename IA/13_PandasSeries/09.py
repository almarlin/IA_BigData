import pandas as pd
import matplotlib.pyplot as plt

dias = [
    "Día 1",
    "Día 2",
    "Día 3",
    "Día 4",
    "Día 5",
    "Día 6",
    "Día 7",
    "Día 8",
    "Día 9",
    "Día 10",
]
visitas = []

print(
    "Introduce el número de visitas diarias a la página web durante los últimos 10 días:"
)

for dia in dias:
    visitas_dia = int(input(f"Visitas en {dia}: "))
    visitas.append(visitas_dia)


visitas_serie = pd.Series(visitas, index=dias)

total_visitas = visitas_serie.sum()
promedio_visitas = visitas_serie.mean()

print(f"\nTotal de visitas: {total_visitas}")
print(f"Promedio de visitas diarias: {promedio_visitas}")

dias_mas_que_promedio = visitas_serie[visitas_serie > promedio_visitas]
print(f"\nDías con más visitas que el promedio:\n{dias_mas_que_promedio}")

visitas_serie = visitas_serie.apply(lambda x: "Baja visita" if x < 50 else x)

print("\nVisitas diarias con valores reemplazados para < 50 visitas:")
print(visitas_serie)

plt.figure(figsize=(10, 6))
visitas_serie.plot(kind="bar", color="lightblue")
plt.title("Número de Visitas Diarias a la Página Web")
plt.xlabel("Días")
plt.ylabel("Visitas")
plt.xticks(rotation=45)
plt.grid(axis="y")
plt.show()
