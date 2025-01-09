numeros1 = list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
numeros2 = list([5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])

maximo = max(numeros1, numeros2)
minimo = min(numeros1, numeros2)

cont = 0

for i in maximo:
    if i in minimo:
        cont += 1

print(f"Coinciden {cont} elementos")