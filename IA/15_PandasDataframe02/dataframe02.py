import pandas as pd  # type: ignore
import numpy as np  # type: ignore

# Mostrar más filas
pd.set_option("display.max_rows", 300)

# Mostrar más columnas
pd.set_option("display.max_columns", 500)

# Nombres alumnos
nombres_alumnos = [
    "Juan Pérez",
    "María López",
    "Carlos García",
    "Ana Fernández",
    "Luis Martínez",
    "Sofía Gómez",
    "Miguel Rodríguez",
    "Laura Sánchez",
    "José Torres",
    "Lucía Morales",
    "Andrés Herrera",
    "Carmen Ruiz",
    "Raúl Castro",
    "Elena Jiménez",
    "Javier Gil",
    "Isabel Romero",
    "Hugo Ortiz",
    "Sara Delgado",
    "Pablo Ramírez",
    "Marta Vargas",
]

# Generar notas aleatorias
notas = {
    "Alumno": nombres_alumnos,
    "Base de Datos": np.random.uniform(1, 10, 20).round(1),
    "Programación": np.random.uniform(1, 10, 20).round(1),
    "Sistemas Informáticos": np.random.uniform(1, 10, 20).round(1),
    "Lenguajes de Marcas": np.random.uniform(1, 10, 20).round(1),
    "Entornos de Desarrollo": np.random.uniform(1, 10, 20).round(1),
}

# DataFrame
df_alumnos = pd.DataFrame(notas)

# Mostrar el DataFrame
print(f"{df_alumnos}\n")

# 1. Renombrar
df_alumnos.rename(
    columns={
        "Base de Datos": "BD",
        "Programación": "PR",
        "Sistemas Informáticos": "SI",
        "Lenguajes de Marcas": "LM",
        "Entornos de Desarrollo": "ED",
    },
    inplace=True,
)
print(f"Renombrados\n{df_alumnos}\n")

# 2. Filtrado
df_suspensosBD = df_alumnos[df_alumnos["BD"] < 5]
df_suspensosBD = df_suspensosBD[["Alumno", "BD"]]
print(f"Suspensos BBDD\n{df_suspensosBD}\n")

df_suspensosPR = df_alumnos[df_alumnos["PR"] < 5]
df_suspensosPR = df_suspensosPR[["Alumno", "PR"]]
print(f"Suspensos Programación\n{df_suspensosPR}\n")


df_sobresalientesBD = df_alumnos[df_alumnos["BD"] > 8]
df_sobresalientesBD = df_sobresalientesBD[["Alumno", "BD"]]

df_sobresalientesPR = df_alumnos[df_alumnos["PR"] > 8]
df_sobresalientesPR = df_sobresalientesPR[["Alumno", "PR"]]

df_sobresalientesSI = df_alumnos[df_alumnos["SI"] > 8]
df_sobresalientesSI = df_sobresalientesSI[["Alumno", "SI"]]

df_sobresalientesLM = df_alumnos[df_alumnos["LM"] > 8]
df_sobresalientesLM = df_sobresalientesLM[["Alumno", "LM"]]

df_sobresalientesED = df_alumnos[df_alumnos["ED"] > 8]
df_sobresalientesED = df_sobresalientesED[["Alumno", "ED"]]

print(f"Sobresalientes en Sistemas\n{df_sobresalientesSI}\n")
df_sobresalientes = df_alumnos[
    (
        (df_alumnos["BD"] > 8)
        | (df_alumnos["PR"] > 8)
        | (df_alumnos["SI"] > 8)
        | (df_alumnos["LM"] > 8)
        | (df_alumnos["ED"] > 8)
    )
]
print(f"Sobresalientes en alguna asignatura\n{df_sobresalientes}\n")

df_marta_carmen = df_alumnos[
    (df_alumnos["Alumno"] == "Marta Vargas") | (df_alumnos["Alumno"] == "Carmen Ruiz")
]
print(f"Resultados filtrados para Marta y Carmen\n{df_marta_carmen}\n")

# 3. Pivotar
asignatura = ["BD", "PR", "SI", "LM", "ED"]
df_pivotado = df_alumnos.melt(
    id_vars=["Alumno"], var_name="Asignatura", value_name="Calificación"
)
print(df_pivotado)

df_pivotado = df_pivotado.pivot_table(
    index="Alumno",
    columns="Asignatura",
    aggfunc="mean",
)
print(df_pivotado)
