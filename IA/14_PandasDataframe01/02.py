import pandas as pd

df = pd.read_excel("datos_alumnos.xlsx")



df.loc[:, "Nota final Programación"] = df.apply(
    lambda x: (x["Programación T1"] + x["Programación T2"] + x["Programación T3"]) / 3,
    axis=1,
)

df.loc[:, "Nota final BBDD"] = df.apply(
    lambda x: (x["Base de Datos T1"] + x["Base de Datos T2"] + x["Base de Datos T3"])
    / 3,
    axis=1,
)

df.loc[:, "Nota final Lenguajes"] = df.apply(
    lambda x: (x["Lenguajes T1"] + x["Lenguajes T2"] + x["Lenguajes T3"]) / 3, axis=1
)

df.loc[:, "Nota final Sistemas"] = df.apply(
    lambda x: (x["Sistemas T1"] + x["Sistemas T2"] + x["Sistemas T3"]) / 3, axis=1
)

df.loc[:, "Nota final Entornos"] = df.apply(
    lambda x: (x["Entornos T1"] + x["Entornos T2"] + x["Entornos T3"]) / 3, axis=1
)


df.loc[:, "Aprobado"] = df.apply(
    lambda x: (
        True
        if (
            (
                x["Nota final Programación"]
                + x["Nota final BBDD"]
                + x["Nota final Lenguajes"]
                + x["Nota final Sistemas"]
                + x["Nota final Entornos"]
            )
            / 5
        )
        > 5
        else False
    )
,axis=1)

print(df[["Nombre","Apellidos","Aprobado"]])
