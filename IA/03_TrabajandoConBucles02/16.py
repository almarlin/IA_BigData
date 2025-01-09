puntaje = int(input("Ingresa un puntaje entre 0 y 100: "))

if puntaje >= 90:
    calificacion = "A"
elif puntaje >= 80:
    calificacion = "B"
elif puntaje >= 70:
    calificacion = "C"
elif puntaje >= 60:
    calificacion = "D"
else:
    calificacion = "F"

print(f"La calificación correspondiente es: {calificacion}")
