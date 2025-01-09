from datetime import datetime

def obtener_fecha_hora_actual():
    fecha_hora_actual = datetime.now()
    fecha_formateada = fecha_hora_actual.strftime("%d/%m/%Y %H:%M:%S")
    return fecha_formateada

print(obtener_fecha_hora_actual())
