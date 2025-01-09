import pandas as pd

data = list()

for i in range(1, 11):
    data.append(float(input(f"Introduce la nota del alumno {i}\n")))

calificaciones = pd.Series(data)

data = list()
for c in calificaciones:
    data.append(input(f"Introduce el nombre del alumno con nota {c}\n"))

calificaciones.index = data

print(f"Promedio: {calificaciones.mean()}")
print(f"Mediana: {calificaciones.median()}")
print(f"Desviación estándar: {calificaciones.std()}")

calificaciones[calificaciones < 50] = "Reprobado"
        
for n,c in calificaciones.items():
    if c != "Reprobado":
        print(f"{n} {c}")