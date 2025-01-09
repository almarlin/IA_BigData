import pandas as pd

df = pd.read_excel("datos_alumnos.xlsx")

df['Programación T3'] = df['Programación T3'].apply(
    lambda x: x + 1 if x < 5 else x
)

df.to_csv("datos_alumnos14.csv")
