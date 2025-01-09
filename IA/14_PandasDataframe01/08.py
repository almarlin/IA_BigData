import pandas as pd

df = pd.read_excel("datos_alumnos.xlsx")

suspensos = df[
    df[
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
            "Entornos T3"
        ]
    ].lt(5).any(axis=1)
    # Menor de 5 y se recogen los que al menos cumplen esta condición 1 vez. Axis indica que se hace en las filas
]

suspensos.to_csv("datos_alumnos08.csv",sep=";")