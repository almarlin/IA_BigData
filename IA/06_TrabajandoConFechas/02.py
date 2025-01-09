from datetime import datetime

def convFecha(fechaStr):
    fecha = datetime.strptime(fechaStr,"%d/%m/%Y")
    return fecha

print(convFecha("08/11/2024"))