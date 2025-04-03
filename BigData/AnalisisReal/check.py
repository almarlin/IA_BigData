import pandas as pd


df = pd.read_csv("muertesINE_stce.csv", delimiter=";")


print(f"Columnas: \n{df.columns}\n")
print(f"Información: \n{df.info()}\n")
print(f"Primeras entradas:\n{df.head()}\n")
print(f"Ejemplos: \n{df.sample(5)}")


df_totales = df[
    (df["Sexo"] == "Ambos sexos")
    | (df["Tamaño de municipio y capital de residencia"] == "Total")
    | (df["Edad"] == "Todas las edades")
]



df = df[~df.index.isin(df_totales.index)]

df["Causas (lista reducida)"] = df["Causas (lista reducida)"].str.strip()

df_ind_totales = df_totales[
    (df_totales["Sexo"] == "Ambos sexos")
    & (df_totales["Tamaño de municipio y capital de residencia"] == "Total")
    & (df_totales["Edad"] == "Todas las edades")
]
df_ind_totales.info()


df_indices = df[df["Causas (lista reducida)"].str.contains(r"\d{3}-\d{3}", regex=True)]


df_indices_totales = df_ind_totales[df_ind_totales["Causas (lista reducida)"].str.contains(r"\d{3}-\d{3}", regex=True)]
df_indices_totales.info()


df = df[~df.index.isin(df_indices_totales.index)]

df_totales = df_totales[~df_totales.index.isin(df_indices_totales.index)]

df_totales.to_csv("muertesINE_totales.csv",index=False)
df_indices_totales.to_csv("muertesINE_totales_por_causa.csv",index=False)
df.to_csv("muertesINE.csv",index=False)
