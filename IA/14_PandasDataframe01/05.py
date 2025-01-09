import pandas as pd

df = pd.read_excel("datos_alumnos.xlsx")

df.loc[:, "Nota final Sistemas"] = df.apply(
    lambda x: (x["Sistemas T1"] + x["Sistemas T2"] + x["Sistemas T3"]) / 3, axis=1
)

print(f"Hay {len(df[df["Nota final Sistemas"] < 5])} alumnos suspensos en Sistemas")