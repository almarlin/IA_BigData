import pandas as pd

df = pd.read_excel("datos_alumnos.xlsx")

df.loc[:, "Promedio general"] = df.apply(
    lambda x: x[
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
    ].sum()
    / 15,
    axis=1
)


print(f"Desviación típica de las notas {df["Promedio general"].std()}")
