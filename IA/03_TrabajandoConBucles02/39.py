numeros = [10, 15, 20, 33, 42, 51, 60, 73, 84, 91]

pares = []
impares = []

for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print("Números pares:", pares)
print("Números impares:", impares)
