numero = int(input("Introduce un numero: "))

numeroStr = str(numero)
i = 0
total = 0

while i < len(numeroStr):
    temp = int(numeroStr[i])
    total += temp
    i += 1

print(f"El total es: {total}")
