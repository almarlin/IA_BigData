import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# El fichero “bancos.csv” contiene las cotizaciones de los principales bancos de
# España con los siguientes datos:
# - Empresa: Nombre de la empresa
# - Apertura: Precio de la acción a la apertura de la Bolsa
# - Máximo: Precio máximo de la acción durante la jornada.
# - Mínimo: Precio mínimo de la acción durante la jornada.
# - Cierre: Precio de la acción al cierre de la Bolsa
# - Volumen: Volumen de negocios al cierre de la Bolsa
# Construir una función que reciba el fichero “bancos.csv” y cree un diagrama de
# líneas con las series temporales de las cotizaciones de cierre de cada banco.

def bancos(path):

    bancos = pd.read_csv(path)

    cierres = bancos.groupby("Empresa")["Cierre"].apply(list)
    cierres = cierres.to_dict()

    empresas = list(cierres.keys())
    cotizaciones = list(cierres.values())
    diagrama = plt.subplot()

    for empresa, cotizacion in zip(empresas, cotizaciones):
        diagrama.plot(cotizacion, label=empresa)

    plt.legend()
    plt.show()


bancos("./ficheros/bancos.csv")