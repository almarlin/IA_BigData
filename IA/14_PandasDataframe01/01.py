import pandas as pd

df = pd.read_excel("datos_alumnos.xlsx")

mayores = df[df["Edad"] >= 20].copy()

mayores.loc[:,"Nota final Programación"] = mayores.apply(
    lambda x: (x["Programación T1"] + x["Programación T2"] + x["Programación T3"]) / 3,
    axis=1,
)

mayores.loc[:,"Nota final BBDD"] = mayores.apply(
    lambda x: (x["Base de Datos T1"] + x["Base de Datos T2"] + x["Base de Datos T3"])
    / 3,
    axis=1,
)

mayores.loc[:,"Nota final Lenguajes"] = mayores.apply(
    lambda x: (x["Lenguajes T1"] + x["Lenguajes T2"] + x["Lenguajes T3"]) / 3, axis=1
)

mayores.loc[:,"Nota final Sistemas"] = mayores.apply(
    lambda x: (x["Sistemas T1"] + x["Sistemas T2"] + x["Sistemas T3"]) / 3, axis=1
)

mayores.loc[:,"Nota final Entornos"] = mayores.apply(
    lambda x: (x["Entornos T1"] + x["Entornos T2"] + x["Entornos T3"]) / 3, axis=1
)


print(
    mayores[
        [
            "Nombre",
            "Apellidos",
            "Nota final Programación",
            "Nota final BBDD",
            "Nota final Lenguajes",
            "Nota final Sistemas",
            "Nota final Entornos",
        ]
    ]
)
