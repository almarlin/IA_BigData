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
# Tenemos que unir las asignaturas bajo el nombre Asignatura para poder hacer la pivotacion correctamente
df_pivotado = df_alumnos.melt(
    id_vars=["Alumno"], var_name="Asignatura", value_name="Calificación"
)

df_pivotado = df_pivotado.pivot_table(
    index="Alumno",
    columns="Asignatura",
    aggfunc="mean",
)
print(f"Pivotado por asignaturas\n{df_pivotado}\n")

# 4. Ordenar
# Ordenado por nombre de alumno
df_ordenado = df_alumnos.sort_values(by=["Alumno"])
print(f"Ordenado por nombre de alumno\n{df_ordenado}\n")
# Ordenado por nota de programacion ascendente
df_ordenado = df_alumnos.sort_values(by=["PR"], ascending=True)
print(f"Ordenado por nota de programacion ascendente\n{df_ordenado}\n")
# Ordenado por nota de base de datps descendente
df_ordenado = df_alumnos.sort_values(by=["BD"], ascending=False)
print(f"Ordenado por nota de base de datos descendente\n{df_ordenado}\n")

# 5. Agrupar
# Promedio de notas de cada alumno
# Es necesario que las calificaciones esten agrupadas en un campo,
# puesto que no se pueden pasar como un array
df_agrupado = df_alumnos.melt(
    id_vars=["Alumno"], var_name="Asignatura", value_name="Calificación"
)
df_agrupado = df_agrupado.groupby(by=["Alumno"])["Calificación"].mean()

print(f"Promedio de notas de cada alumno\n{df_agrupado}\n")

# Promedio de notas por asignatura
df_agrupado = df_alumnos.melt(
    id_vars=["Alumno"], var_name="Asignatura", value_name="Calificación"
)
df_agrupado = df_agrupado.groupby(by=["Asignatura"])["Calificación"].mean()
print(f"Promedio de notas por asignatura\n{df_agrupado}\n")

# Alumno con mejor promedio
df_agrupado = df_alumnos.melt(
    id_vars=["Alumno"], var_name="Asignatura", value_name="Calificación"
)
df_agrupado = df_agrupado.groupby(by=["Alumno"])["Calificación"].mean()
mejor_alumo = df_agrupado.sort_values(ascending=False).head(1)
print(f"Alumno con mejor promedio\n{mejor_alumo}\n")

# 6. Concatenar

# Generar índices aleatorios para hacer NaN
porcentaje_faltante = 0.2
total_celdas = df_alumnos.shape[0] * df_alumnos.shape[1] - df_alumnos.shape[0]
total_faltantes = int(total_celdas * porcentaje_faltante)

indices_faltantes = np.random.choice(
    df_alumnos.index.repeat(df_alumnos.shape[1] - 1), total_faltantes, replace=True
)
columnas_faltantes = np.random.choice(
    df_alumnos.columns[1:], total_faltantes, replace=True
)  # Excluyendo 'Alumno'

df_huecos = df_alumnos.copy()
for i, col in zip(indices_faltantes, columnas_faltantes):
    df_huecos.loc[i, col] = np.nan

df_completo = pd.concat(
    [df_alumnos, df_huecos],
    ignore_index=True,
)
print(f"DF con datos completos y faltantes\n{df_completo}\n")

df_completo = df_completo[
    df_completo["BD"].notna()
    & df_completo["PR"].notna()
    & df_completo["LM"].notna()
    & df_completo["SI"].notna()
    & df_completo["ED"].notna() 
]
print(f"DF filtrado\n{df_completo}\n")

