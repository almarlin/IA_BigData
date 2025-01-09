import random

def primitiva():
    numeros = list()
    for i in range (1,7):
        numeros.append(random.randint(1,49))

    complementario = random.randint(0,9)
    reintegro = random.randint(0,9)

    primitiva = list([numeros,complementario,reintegro])

    return primitiva

apuesta = list()

while len(apuesta) < 7:
    print(f"Número {len(apuesta)}")
    num = int(input("Introduce un número entre 1 y 49:\n"))
    if num < 50 and num > 0:
        apuesta.append(num)
    else:
        print("Número no permitido.")

while True:
    compl = int(input("Introduce el complementario:\n"))
    if compl > 0 and compl < 10:
        break
    else:
        print("Número inválido.")


while True:
    reintegro = int(input("Introduce el reintegro:\n"))
    if reintegro > 0 and reintegro < 10:
        break
    else:
        print("Número inválido.")


print("------------------------------------------------------------------------------")
print(f"Tu apuesta es: {apuesta}\nNúmero complementario: {compl}\nReintegro: {reintegro}")
print("------------------------------------------------------------------------------")

resultado = primitiva()

print(f"Los números premiados de la primitiva son: {resultado[0]}")
print(f"El número complementario es: {resultado[1]}")
print(f"El reintegro es: {resultado[2]}")

if resultado[0] == apuesta:
    print("¡Has ganado la primitiva!")
else:
    print("No ha habido suerte esta vez.")

if resultado[1] == compl:
    print("¡Acertaste el complementario!")

if resultado[2] == reintegro:
    print("¡Acertaste el reintegro!")
