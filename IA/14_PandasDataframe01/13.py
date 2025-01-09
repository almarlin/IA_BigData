import pandas as pd

df = pd.read_excel("datos_alumnos.xlsx")

mayores = df[df["Edad"]>22]

mayores.to_excel("datos_alumnos13.xlsx",index=None)