import pandas as pd

horas_trabajadas = []
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

print("Introduce las horas trabajadas por el empleado durante los 5 días laborales:")

for dia in dias:
    horas = float(input(f"Horas trabajadas el {dia}: "))
    horas_trabajadas.append(horas)

horas_serie = pd.Series(horas_trabajadas, index=dias)

total_horas = horas_serie.sum()

dias_mas_8_horas = horas_serie[horas_serie > 8].index.tolist()

horas_serie_reemplazadas = horas_serie.apply(lambda x: "Medio tiempo" if x < 6 else x)

def clasificar_horas(x):
    if x < 6:
        return "Medio tiempo"
    elif x > 8:
        return "Extra"
    else:
        return "Normal"

clasificacion_horas = horas_serie.apply(clasificar_horas)

print(f"\nTotal de horas trabajadas: {total_horas}")
print(f"Días en los que se trabajaron más de 8 horas: {dias_mas_8_horas}")
print("\nClasificación de horas trabajadas:")
print(clasificacion_horas)
