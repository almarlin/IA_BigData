import pandas as pd

# Cargar los datos desde el Excel
def cargar_datos(file_path):
    df = pd.read_excel(file_path)
    # Reemplazar valores nulos con un indicador
    df.fillna({
        'Marca': 'Desconocida',
        'Modelo': 'Desconocido',
        'Color': 'Desconocido',
        'Motor': 'Desconocido',
        'Combustible': 'Desconocido'
    }, inplace=True)
    df.fillna(0, inplace=True)  # Reemplazar otros nulos con 0
    return df

data = cargar_datos("vehiculos.xlsx")

# Edición y verificación de datos
def verificar_datos(df):
    print("Total de registros cargados:", len(df))
    print("Vista previa de los datos:\n", df.head())

verificar_datos(data)

# Análisis estadístico
def analisis_estadistico(df):
    estadisticas = {
        'Promedio_Precio': df['Precio'].mean(),
        'Promedio_Kilómetros': df['Kilómetros'].mean(),
        'Máximo_Precio': df['Precio'].max(),
        'Mínimo_Precio': df['Precio'].min()
    }
    estadisticas_df = pd.DataFrame([estadisticas])
    estadisticas_df.to_excel("estadisticas_vehiculos.xlsx", index=False)
    print("Análisis estadístico guardado en estadisticas_vehiculos.xlsx")

analisis_estadistico(data)

# Filtrado de datos
def filtrar_vehiculos(df, **kwargs):
    filtro = df
    for clave, valor in kwargs.items():
        filtro = filtro[filtro[clave] == valor]
    print(f"Vehículos filtrados por {kwargs}:\n", filtro)
    return filtro

# Ejemplo: Filtrar por marca y modelo
filtrar_vehiculos(data, Marca='Toyota', Modelo='Auris')

# Ordenar datos
def ordenar_datos(df, columna, ascendente=True):
    df_ordenado = df.sort_values(by=columna, ascending=ascendente)
    print(f"Datos ordenados por {columna}:\n", df_ordenado.head())
    return df_ordenado

# Ejemplo: Ordenar por precio
datos_ordenados = ordenar_datos(data, 'Precio')

# Transformar datos
def transformar_datos(df):
    df['Depreciación'] = 2024 - df['Anyo']  # Agregar columna de depreciación
    df.to_csv("vehiculos_transformados.csv", index=False)
    print("Datos transformados y guardados en vehiculos_transformados.csv")

transformar_datos(data)