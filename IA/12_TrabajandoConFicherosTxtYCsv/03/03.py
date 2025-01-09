import csv

def csv_to_dict(path):
    with open(path,"r",encoding="utf-8") as f:
        data =csv.reader(f,delimiter=";")

        ibex = {'Nombre': [], 'Final': [], 'Máximo': [], 'Mínimo': [], 'Volumen': [], 'Efectivo': []}
        for i,d in enumerate(data):
            if i != 0:
                d[1]=float(d[1].replace(".", "").replace(",", "."))
                d[2]=float(d[2].replace(".", "").replace(",", "."))
                d[3]=float(d[3].replace(".", "").replace(",", "."))
                d[4]=float(d[4].replace(".", "").replace(",", "."))
                d[5]=float(d[5].replace(".", "").replace(",", "."))
                ibex['Nombre'].append(d[0])
                ibex['Final'].append(float(d[1]))
                ibex['Máximo'].append(float(d[2]))
                ibex['Mínimo'].append(float(d[3]))
                ibex['Volumen'].append(float(d[4]))
                ibex['Efectivo'].append(float(d[5]))
    return  ibex

ibexDict = csv_to_dict("cotizacion.csv")
    
def dict_to_csv(path,data):
    resumen = {'Columna': ['Final', 'Máximo', 'Mínimo', 'Volumen', 'Efectivo'],
        'Mínimo': [
            min(data['Final']),
            min(data['Máximo']),
            min(data['Mínimo']),
            min(data['Volumen']),
            min(data['Efectivo'])
        ],
        'Máximo': [
            max(data['Final']),
            max(data['Máximo']),
            max(data['Mínimo']),
            max(data['Volumen']),
            max(data['Efectivo'])
        ],
        'Media': [
            sum(data['Final']) / len(data['Final']),
            sum(data['Máximo']) / len(data['Máximo']),
            sum(data['Mínimo']) / len(data['Mínimo']),
            sum(data['Volumen']) / len(data['Volumen']),
            sum(data['Efectivo']) / len(data['Efectivo'])
        ]
    }

    with open(path,"w",encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=['Columna', 'Mínimo', 'Máximo', 'Media'])

        writer.writeheader()

        # Escribir los datos de las columnas
        for i in range(len(resumen['Columna'])):
            writer.writerow({
                'Columna': resumen['Columna'][i],
                'Mínimo': resumen['Mínimo'][i],
                'Máximo': resumen['Máximo'][i],
                'Media': resumen['Media'][i]
            })
        

dict_to_csv("cotizacion_dict.csv",ibexDict)