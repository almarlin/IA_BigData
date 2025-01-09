from datetime import datetime

def restarFechas(f1,f2):
    fecha1 = datetime.strptime(f1,"%d/%m/%Y")
    fecha2 = datetime.strptime(f2,"%d/%m/%Y")

    dif = fecha1 - fecha2

    return dif.days

print(restarFechas("08/11/2024", "01/11/2024"))