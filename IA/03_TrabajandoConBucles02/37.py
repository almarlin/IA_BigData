import random

while True:
    numero = random.randint(0, 10)  # Genera un número aleatorio entre 0 y 10
    print(numero)
    if numero == 0:
        print("Se ha generado un cero. Terminando el programa.")
        break
