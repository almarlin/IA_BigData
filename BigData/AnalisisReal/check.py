import pandas as pd


df = pd.read_csv("muertesINE_stce.csv", delimiter=";",thousands='.')


print(f"Columnas: \n{df.columns}\n")
print(f"Información: \n{df.info()}\n")
print(f"Primeras entradas:\n{df.head()}\n")
print(f"Ejemplos: \n{df.sample(5)}")

# Se recogen los registros que agrupen en algún campo
df_totales = df[
    (df["Sexo"] == "Ambos sexos")
    | (df["Tamaño de municipio y capital de residencia"] == "Total")
    | (df["Edad"] == "Todas las edades")
]

# Se eliminan los registros agrupadores del dataset principal
df = df[~df.index.isin(df_totales.index)]

df["Causas (lista reducida)"] = df["Causas (lista reducida)"].str.strip()

# Se recogen los totales de las causas especificas
df_ind_totales = df_totales[
    (df_totales["Sexo"] == "Ambos sexos")
    & (df_totales["Tamaño de municipio y capital de residencia"] == "Total")
    & (df_totales["Edad"] == "Todas las edades")
]


df_ind_totales.info()
df_indices = df[df["Causas (lista reducida)"].str.contains(r"\d{3}-\d{3}", regex=True)]




# Se recogen los totales de indices generales
df_indices_totales = df_ind_totales[
    df_ind_totales["Causas (lista reducida)"].str.contains(r"\d{3}-\d{3}", regex=True)
]



# Se elimina el indice de todas las causas
df_indices_totales = df_indices_totales[
    ~(
        df_indices_totales["Causas (lista reducida)"]
        == "001-102 I-XXII.Todas las causas"
    )
]
df_indices_totales.info()

# Se recogen los registros de todas las causas
df_total = (df_totales[(df_totales["Causas (lista reducida)"] == "001-102 I-XXII.Todas las causas")])

df = df[~df.index.isin(df_indices.index)]

df_totales = df_totales[~df_totales.index.isin(df_indices_totales.index)]


df_indices = df_indices[~df_indices.index.isin(df_ind_totales.index)]
df_indices = (df_indices[~(df_indices["Causas (lista reducida)"] == "001-102 I-XXII.Todas las causas")])


df_indices.to_csv("muertesINE_causas_generales.csv",index=False)
df_total.to_csv("muertesINE_todas_las_causas.csv",index=False)
df_totales.to_csv("muertesINE_totales.csv", index=False)
df_indices_totales.to_csv("muertesINE_totales_por_causa.csv", index=False)
df.to_csv("muertesINE.csv", index=False)
