# 20. Exporta un DataFrame a Excel y asegúrate de formatear los valores de las notas con dos decimales.

import pandas as pd

df = pd.read_excel("datos_alumnos.xlsx")


df.loc[:,"Promedio"] = df[
    [
        "Programación T1",
        "Programación T2",
        "Programación T3",
        "Base de Datos T1",
        "Base de Datos T2",
        "Base de Datos T3",
        "Lenguajes T1",
        "Lenguajes T2",
        "Lenguajes T3",
        "Sistemas T1",
        "Sistemas T2",
        "Sistemas T3",
        "Entornos T1",
        "Entornos T2",
        "Entornos T3",
    ]
].mean(axis=1)

df["Promedio"] = df["Promedio"].round(2)

df.to_excel("datos_alumnos20.xlsx")