from datetime import datetime
from datetime import timedelta

def sumarDias(fecha, dias):
    f = datetime.strptime(fecha,"%d/%m/%Y")

    return f + timedelta(days=dias)

print(sumarDias("08/11/2024", 31))

