import random
adivinado = False
num = random.randint(1,100)

while adivinado == False:
    intento = int(input("Intenta adivinar el número secreto (1-100): "))

    if intento == num:
        adivinado = True
        print("¡Adivinaste el número!")
    elif intento < num:
        print(f"El número es mayor.")
    elif intento > num:
        print(f"El número es menor.")