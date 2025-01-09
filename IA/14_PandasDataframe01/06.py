import pandas as pd

df = pd.read_excel("datos_alumnos.xlsx")

df.loc[:, "Nota final Programación"] = df.apply(
    lambda x: (x["Programación T1"] + x["Programación T2"] + x["Programación T3"]) / 3,
    axis=1,
)

# idxmax() devuelve el indice del valor maximo de la seleccion
alumno_mejor_programacion = df.loc[df["Nota final Programación"].idxmax()]
print(alumno_mejor_programacion)
