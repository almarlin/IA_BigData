import pandas as pd

import pandas as pd

dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
data = []

print("Introduce las precipitaciones registradas durante los últimos 7 días (en mm):")

for dia in dias:
    precipitacion = float(input(f"Precipitación en {dia}: "))
    data.append(precipitacion)


precipitaciones = pd.Series(data, index=dias)

print("\nPrecipitaciones de los últimos 7 días:")
print(precipitaciones)

precipitaciones_text = precipitaciones.apply(lambda x: "Sin precipitación" if x == 0 else x)
print("\nPrecipitaciones de los últimos 7 días:")
print(precipitaciones_text)

print(f"Total de precipitaciones {precipitaciones.sum()}")
print(f"Promedio de precipitaciones {precipitaciones.mean()}")
print("\nPrecipitaciones por encima del promedio:")
print(precipitaciones[precipitaciones > precipitaciones.mean()])
