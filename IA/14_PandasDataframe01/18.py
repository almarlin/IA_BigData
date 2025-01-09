import pandas as pd

df = pd.read_excel("datos_alumnos.xlsx")

minProg = df["Programación T3"].min()
minBD = df["Base de Datos T3"].min()
minLen = df["Lenguajes T3"].min()
minSis = df["Sistemas T3"].min()
minEnt = df["Entornos T3"].min()

notasMinimas = {
    "Nota mínima de Programación": [minProg],
    "Nota mínima de BBDD": [minBD],
    "Nota mínima de Lenguajes": [minLen],
    "Nota mínima de Sistemas": [minSis],
    "Nota mínima de Entornos": [minEnt]
}

dfNotas = pd.DataFrame(notasMinimas)

dfNotas.to_csv("notas18.csv")