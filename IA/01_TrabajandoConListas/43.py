numeros = list([234, 135, 12, 0, 56, 7, 32, 35, 3])

pares = list()

for num in numeros:
    if num % 2 == 0:
        pares.append(num)

print("Todos: ",numeros)
print("Pares: ",pares)