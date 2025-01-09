numeros = list()

while True:
    num = int(input("Si deseas finalizar el proceso inserta un 0. En cualquier otro caso, inserta un número: "))

    if num == 0:
        break

    numeros.append(num)

promedio = 0
tot = 0
for n in numeros:
    tot+=n

promedio = tot / len(numeros)

print(f"Los números introducidos son: {numeros}")
print(f"El promedio de los números introducidos es: {promedio}")