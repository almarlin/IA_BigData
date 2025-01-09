import random

num = int(input("Introduce un numero del 1 al 10: "))

intentos = 1

while intentos < 5:
    ad = random.randint(1,10)
    if ad == num:
        print(f"¡Numero adivinado!: {ad}")
        break
    else:
        intentos+=1
else:
    print("Número no adivinado.")