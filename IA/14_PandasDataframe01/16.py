import pandas as pd

df = pd.read_excel("datos_alumnos.xlsx")

mayores = df[df["Edad"] > 23]
menores = df[df["Edad"] <= 23]

mayores.loc[:,"Promedio"] = mayores[
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

menores.loc[:,"Promedio"] = mayores[
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

mayores.to_excel("mayores16.xlsx",index=None)
menores.to_excel("menores16.xlsx",index=None)