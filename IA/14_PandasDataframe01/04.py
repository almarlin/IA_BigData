import pandas as pd

df = pd.read_excel("datos_alumnos.xlsx")
df.loc[:, "Nota final Lenguajes"] = df.apply(
    lambda x: (x["Lenguajes T1"] + x["Lenguajes T2"] + x["Lenguajes T3"]) / 3, axis=1
)
print(df[df["Nota final Lenguajes"]])