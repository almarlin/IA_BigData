numeros = list([234, 135, 12, 5, 56, 7, 32, 35, 3])

mayor = 0

for num in numeros:
    if num > mayor:
        mayor = num

print(f"El numero mayor de la lista es {mayor}.")