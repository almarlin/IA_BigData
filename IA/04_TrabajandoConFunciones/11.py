def segundosTotales(h,m,s):
    minTot = h*60 + m
    segTot = minTot*60 +s
    return segTot

horas = float(input("Introduce las horas: "))
minutos = float(input("Introduce los minutos: "))
segundos = float(input("Introduce los segundos: "))

print(f"El tiempo total en segundo es: {segundosTotales(horas,minutos,segundos)}")