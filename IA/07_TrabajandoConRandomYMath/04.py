import random
from time import sleep

for i in range(3):  # Puedes cambiar el rango para el número de repeticiones
    print("Dando vueltas...")
    sleep(1)  # Pausa de 1 segundo entre cada mensaje

ruleta = random.randint(0, 36)

print("Ruleta girada.")

num = int(input("¿Cuál es el número premiado? "))

if num == ruleta:
    print("¡Acertaste!")
else:
    print("No has acertado")

print(f"El número premiado es: {ruleta}")

if ruleta == 0:
    print(f"Gana la banca")
elif ruleta % 2 == 0:
    print(f"Rojo")
else:
    print(f"Negro")
