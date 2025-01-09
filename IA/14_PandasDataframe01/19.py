import pandas as pd

dfMayores = pd.read_excel("mayores16.xlsx")
dfMenores = pd.read_excel("menores16.xlsx")

df = pd.concat([dfMayores,dfMenores],ignore_index=True)

df.to_excel("datos_alumnos19.xlsx")