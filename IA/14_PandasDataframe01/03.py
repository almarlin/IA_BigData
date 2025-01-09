import pandas as pd

df = pd.read_excel("datos_alumnos.xlsx")

# Axis=0 selecciona la columna y max() el valor maximo de la seleccion
max_notas = {
    "Programación": df[["Programación T1", "Programación T2", "Programación T3"]].max(axis=0).max(),
    "BBDD": df[["Base de Datos T1", "Base de Datos T2", "Base de Datos T3"]].max(axis=0).max(),
    "Lenguajes": df[["Lenguajes T1", "Lenguajes T2", "Lenguajes T3"]].max(axis=0).max(),
    "Sistemas": df[["Sistemas T1", "Sistemas T2", "Sistemas T3"]].max(axis=0).max(),
    "Entornos": df[["Entornos T1", "Entornos T2", "Entornos T3"]].max(axis=0).max()
}

print("Nota máxima de cada módulo:")
for modulo, max_nota in max_notas.items():
    print(f"{modulo}: {max_nota}")
