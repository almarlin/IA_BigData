import pandas as pd

df = pd.read_csv("datos_alumnos14.csv")

# El primer mean devuelve el promedio de cada alumno en el modulo, el segundo el promedio del grupo
print(f"Promedio notas Programación: {df[["Programación T1","Programación T2","Programación T3"]].mean(axis=1).mean()}")

