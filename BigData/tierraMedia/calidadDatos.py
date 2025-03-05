import pandas as pd
import numpy as np
import re
from unidecode import unidecode
from dateutil import parser
from datetime import datetime

# Crear dataset ficticio
data = {
    "ID_Batalla": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Nombre_Batalla": [
        "Abismo de Helm",
        "Minas Tirith",
        "Batalla de los Campos del Pelennor",
        "Batalla del Morannon",
        "Batalla de Cuernavilla",
        "Batalla de Lothlórien",
        "Batalla de Erebor",
        "Batalla de Dale",
        "Batalla de la Puerta Negra",
        "Batalla de Bywater",
    ],
    "Fecha": [
        "3019-03-03",
        "3019-03-15",
        "3019-03-15",
        "3019-03-25",
        "3019-03-03",
        "3019-03-22",
        "3019-03-17",
        "3019-03-17",
        "3019-03-25",
        "03/11/3019",
    ],  # Formato inconsistente
    "Lugar": [
        "Abismo de Helm",
        "Minas Tirith",
        "Campos del Pelennor",
        "Morannon",
        "Cuernavilla",
        "Lothlórien",
        "Erebor",
        "Dale",
        "Puerta Negra",
        "Bywater",
    ],
    "Bando": [
        "Comunidad del Anillo",
        "Comunidad del Anillo",
        "Comunidad del Anillo",
        "Comunidad del Anillo",
        "Comunidad del Anillo",
        "Saurón",
        "Sauron",
        "Saruman",
        "Saurón",
        "Comunidad del Anillo",
    ],  # Error tipográfico
    "Líder": [
        "Aragorn",
        "Gandalf",
        "Théoden",
        "Aragorn",
        np.nan,
        np.nan,
        "Sauron",
        "Saruman",
        "Sauron",
        "Sam",
    ],  # Valores faltantes
    "Bajas_Enemigas": [
        10000,
        50000,
        -1000,
        70000,
        8000,
        2000,
        1000000,
        4000,
        5000,
        100,
    ],  # Valor negativo y atípico
    "Bajas_Propias": [
        500,
        2000,
        3000,
        4000,
        np.nan,
        5000,
        6000,
        7000,
        8000,
        10,
    ],  # Valor faltante
    "Victoria": [
        "Sí",
        "Sí",
        "Sí",
        "Sí",
        "Sí",
        "No",
        "Tal vez",
        "No",
        "No",
        "Sí",
    ],  # Valor incorrecto
    "Anotaciones": [
        "Victoria decisiva",
        "Derrota de Sauron",
        "Derrota de los Nazgûl",
        "Destrucción del Anillo",
        "Defensa exitosa",
        "Ataque repelido",
        "Ataque repelido",
        "Ataque repelido",
        "Ataque repelido",
        "Victoria en la Comarca",
    ],
}

df = pd.DataFrame(data)

# Mostrar dataset con problemas de calidad
print("Dataset con problemas de calidad:")
print(df)

# VALORES FALTANTES --------------------------------------------

print(f"\nRegistros con valores nulos:\n{df[df.isnull().any(axis=1)]}")

nulos_por_columna = df.isnull().sum()
print("Columnas con valores nulos:")
print(nulos_por_columna)

# Eliminamos los registros incompletos.
df = df.dropna()

#  INCONSISTENCIAS Y ERRORES TIPOGRAFICOS ----------------------

# Poner en minuscula
df["Nombre_Batalla"] = df["Nombre_Batalla"].str.lower()
df["Líder"] = df["Líder"].str.lower()
df["Bando"] = df["Bando"].str.lower()
df["Lugar"] = df["Lugar"].str.lower()
# Eliminar acentos
df["Nombre_Batalla"] = df["Nombre_Batalla"].apply(
    lambda x: unidecode(str(x)) if isinstance(x, str) else x
)
df["Líder"] = df["Líder"].apply(
    lambda x: unidecode(str(x)) if isinstance(x, str) else x
)
df["Bando"] = df["Bando"].apply(
    lambda x: unidecode(str(x)) if isinstance(x, str) else x
)
df["Lugar"] = df["Lugar"].apply(
    lambda x: unidecode(str(x)) if isinstance(x, str) else x
)
# Eliminar puntuaciones
df["Nombre_Batalla"] = df["Nombre_Batalla"].apply(
    lambda x: re.sub(r"[^a-zA-Z0-9\s]", "", str(x))
)
df["Líder"] = df["Líder"].apply(lambda x: re.sub(r"[^a-zA-Z0-9\s]", "", str(x)))
df["Bando"] = df["Bando"].apply(lambda x: re.sub(r"[^a-zA-Z0-9\s]", "", str(x)))
df["Lugar"] = df["Lugar"].apply(lambda x: re.sub(r"[^a-zA-Z0-9\s]", "", str(x)))
#  VALORES ATÍPICOS --------------------------------------------

q1 = df["Bajas_Propias"].quantile(0.25)
q3 = df["Bajas_Propias"].quantile(0.75)

intercuartil = q3 - q1
outliers = df[
    (df["Bajas_Propias"] < (q1 - 1.5 * intercuartil))
    | (df["Bajas_Propias"] > (q3 + 1.5 * intercuartil))
]

print(f"Valores atípicos de Bajas propias:\n{outliers['Bajas_Propias']}\n")

q1 = df["Bajas_Enemigas"].quantile(0.25)
q3 = df["Bajas_Enemigas"].quantile(0.75)

intercuartil = q3 - q1
outliers = df[
    (df["Bajas_Enemigas"] < (q1 - 1.5 * intercuartil))
    | (df["Bajas_Enemigas"] > (q3 + 1.5 * intercuartil))
]
print(f"Valores atípicos de Bajas enemigas:\n{outliers['Bajas_Enemigas']}\n")

df["Bajas_Enemigas"] = df["Bajas_Enemigas"].apply(
    lambda bajas: bajas * -1 if bajas < 0 else bajas
)
df["Bajas_Propias"] = df["Bajas_Propias"].apply(
    lambda bajas: bajas * -1 if bajas < 0 else bajas
)
# ERRORES DE FORMATOS -----------------------------------------
df["Fecha"] = df["Fecha"].apply(lambda fecha: parser.parse(fecha))
df["Fecha"] = df["Fecha"].apply(lambda fecha: datetime.strftime(fecha, "%Y-%m-%d"))

# Comprobamos que hay una victoria con mal formato
print(f"Resultados mal guardados\n{df[df['Victoria'].apply(lambda victoria: victoria not in ('Sí', 'No', 'Empate'))]}\n")
# En este caso al tener las anotaciones podemos ver que se repelió el ataque, por lo tanto vamos a considerarlo una derrota
df["Victoria"] = df['Victoria'].apply(lambda victoria: "No" if victoria not in ('Sí', 'No', 'Empate') else victoria)

# DATASET FINAL -----------------------------------------------

print(df)
